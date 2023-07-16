import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

def subscribe_topic_message(self, msg):
    Node.get_logger('test').info('Received message: {0}'.format(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = Node('Helloworld_subscriber')
    qos_profile = QoSProfile(depth=10)
    helloworld_subscriber = node.create_subscription(
      String,
      'helloworld',
      subscribe_topic_message,
      qos_profile)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
  main()