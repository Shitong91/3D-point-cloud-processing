#include <ros/ros.h>
#include "loam_velodyne/MultiScanRegistration.h"


/** Main node entry point. */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "scanRegistration");
  ros::NodeHandle node;
  ros::NodeHandle privateNode("~");

  loam::MultiScanRegistration multiScan;   //表示使用不带参数的构造函数，或者有默认参数值的构造函数。

  if (multiScan.setup(node, privateNode)) {
    // initialization successful
    ros::spin();
  }

  return 0;
}
