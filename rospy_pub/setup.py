from setuptools import setup
from setuptools import find_packages

package_name = 'rospy_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thiago',
    maintainer_email='thiago@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'helloworld_publisher = rospy_pub.helloworld_publisher:main',
            'helloworld_subscriber = rospy_pub.helloworld_subscriber:main',
        ],
    },
)