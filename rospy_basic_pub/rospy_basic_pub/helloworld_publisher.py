import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

count = 0

def publish_helloworld_msg(helloworld_publisher):
    global count
    msg = String()
    msg.data = 'Hello World : {0}'.format(count)
    helloworld_publisher.publish(msg)
    Node.get_logger('test').info('Published message : {0}'.format(msg.data))
    count += 1


def main(args=Node):
    rclpy.init(args=args)
    node = Node('helloworld_publisher')
    qos_profile = QoSProfile(depth=10)
    helloworld_publisher = node.create_publisher(String, 'helloworld', qos_profile)
    timer = node.create_timer(1, lambda: publish_helloworld_msg(helloworld_publisher))

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

    return

if __name__=='__main__':
    main()