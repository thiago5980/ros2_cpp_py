#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

int main(int argc, char* argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<rclcpp::Node>("helloworld_publisher");
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr helloworld_publisher;
  rclcpp::TimerBase::SharedPtr timer;
  auto qos_profile = rclcpp::QoS(rclcpp::KeepLast(10));
  size_t count;
  helloworld_publisher = node->create_publisher<std_msgs::msg::String>(
    "helloworld", qos_profile);
  timer = node->create_wall_timer(
    1s, [node, helloworld_publisher, &count]()->void
    {
        auto msg = std_msgs::msg::String();
        msg.data = "Hello World2: " + std::to_string(count++);
        RCLCPP_INFO(node->get_logger(), "Published message: '%s'", msg.data.c_str());
        helloworld_publisher->publish(msg);
    }
  );
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}