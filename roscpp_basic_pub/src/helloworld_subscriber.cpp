#include <functional>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

void subscribe_topic_message(const std_msgs::msg::String::SharedPtr msg)
{
  RCLCPP_INFO(rclcpp::get_logger("test"), "Received message: '%s'", msg->data.c_str());
}

int main(int argc, char* argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<rclcpp::Node>("Helloworld_subscriber");
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr helloworld_subscriber;
  auto qos_profile = rclcpp::QoS(rclcpp::KeepLast(10));
  helloworld_subscriber = node->create_subscription<std_msgs::msg::String>(
    "helloworld",
    qos_profile,
    subscribe_topic_message);
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}