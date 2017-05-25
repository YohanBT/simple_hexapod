#!/usr/bin/env python

import rospy
from simple_hexapod_gazebo.simple_hexapod import Simple_Hexapod


if __name__ == '__main__':
    rospy.init_node('walker_demo')

    rospy.loginfo('Instantiating robot Client')
    robot = Simple_Hexapod()
    rospy.sleep(1)

    rospy.loginfo('Walker Demo Starting')

    #robot.set_walk_velocity(0.2, 0, 0)
    #print(robot.get_angles())
    #rospy.sleep(3)
    #print(robot.get_angles())
    # robot.set_walk_velocity(1, 0, 0)
    # rospy.sleep(3)
    # robot.set_walk_velocity(0, 1, 0)
    # rospy.sleep(3)
    # robot.set_walk_velocity(0, -1, 0)
    # rospy.sleep(3)
    # robot.set_walk_velocity(-1, 0, 0)
    # rospy.sleep(3)
    # robot.set_walk_velocity(1, 1, 0)
    #rospy.sleep(5)
    robot.set_walk_velocity(0, 0, 0)
    #rospy.loginfo(robot.get_angles())
    #set angles
    angles = {'j_thigh_rf': -1.24990536501484328, 'j_thigh_lf': -1.15608529760143774}
    robot.set_angles(angles)
    #robot. print_joints()
    rospy.loginfo('Walker Demo Finished')


# {'j_thigh_rf': -0.24990536501484328, 'j_thigh_lf': -0.15608529760143774, 'j_c1_rf': -0.07129160722702554, 'j_tibia_lm': -0.201888311751377, 'j_tibia_rr': -0.2132340636006953, 'j_c1_rm': 0.07203264600575654, 'j_thigh_lm': -0.252734632888024, 'j_thigh_rm': -0.13804806269933945, 'j_c1_lr': -0.0729509653878333, 'j_tibia_lf': -0.15586225242546536, 'j_tibia_rf': -0.22917224322151064, 'j_c1_lm': 0.06974053728245622, 'j_thigh_rr': -0.24867630325402068, 'j_thigh_lr': -0.14734538480970105, 'j_c1_rr': -0.07066058456034074, 'j_c1_lf': -0.07224373161680564, 'j_tibia_rm': -0.11788945006839491, 'j_tibia_lr': -0.11951994280148703}
# {'j_thigh_rf': -0.07930532940456203, 'j_thigh_lf': -0.26464759922046355, 'j_c1_rf': -0.07325845548838039, 'j_tibia_lm': -0.010623574245189005, 'j_tibia_rr': -0.017688187715007686, 'j_c1_rm': 0.07431287766934513, 'j_thigh_lm': -0.08720048814693193, 'j_thigh_rm': -0.26221572309378427, 'j_c1_lr': -0.0742664401111055, 'j_tibia_lf': -0.24194072163963298, 'j_tibia_rf': -0.031089986316159113, 'j_c1_lm': 0.07114969180851904, 'j_thigh_rr': -0.07774360622216925, 'j_thigh_lr': -0.2663331378299407, 'j_c1_rr': -0.07257285766243093, 'j_c1_lf': -0.07429764533757766, 'j_tibia_rm': -0.2406217226165701, 'j_tibia_lr': -0.24274438943463927}
# {'j_thigh_rf': -0.07581114678368461, 'j_thigh_lf': -0.24741660557992518, 'j_c1_rf': -0.3725146295248134, 'j_tibia_lm': -0.02415418088135457, 'j_tibia_rr': -0.023762082179837662, 'j_c1_rm': 0.3714365401860542, 'j_thigh_lm': -0.09212832883787936, 'j_thigh_rm': -0.24937921084468062, 'j_c1_lr': -0.37123285919288396, 'j_tibia_lf': -0.2626502272152047, 'j_tibia_rf': -0.11024750202039346, 'j_c1_lm': 0.36741319792774796, 'j_thigh_rr': -0.08618148348001853, 'j_thigh_lr': -0.24972359910759412, 'j_c1_rr': -0.36681858291563163, 'j_c1_lf': -0.37127896021030793, 'j_tibia_rm': -0.222841141708507, 'j_tibia_lr': -0.23408873912614503}