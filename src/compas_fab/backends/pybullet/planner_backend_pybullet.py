from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fab.backends.client import PlannerInterface
from compas_fab.backends.pybullet.backend_features.pybullet_add_attached_collision_mesh import PyBulletAddAttachedCollisionMesh
from compas_fab.backends.pybullet.backend_features.pybullet_forward_kinematics import PyBulletForwardKinematics
from compas_fab.backends.pybullet.backend_features.pybullet_inverse_kinematics import PyBulletInverseKinematics
from compas_fab.backends.pybullet.backend_features.pybullet_add_collision_mesh import PyBulletAddCollisionMesh
from compas_fab.backends.pybullet.backend_features.pybullet_append_collision_mesh import PyBulletAppendCollisionMesh
from compas_fab.backends.pybullet.backend_features.pybullet_remove_attached_collision_mesh import PyBulletRemoveAttachedCollisionMesh
from compas_fab.backends.pybullet.backend_features.pybullet_remove_collision_mesh import PyBulletRemoveCollisionMesh


class PyBulletPlanner(PlannerInterface):
    def __init__(self, client):
        super(PyBulletPlanner, self).__init__(client)
        self.add_attached_collision_mesh = PyBulletAddAttachedCollisionMesh(self.client)
        self.add_collision_mesh = PyBulletAddCollisionMesh(self.client)
        self.append_collision_mesh = PyBulletAppendCollisionMesh(self.client)
        self.remove_collision_mesh = PyBulletRemoveCollisionMesh(self.client)
        self.remove_attached_collision_mesh = PyBulletRemoveAttachedCollisionMesh(self.client)
        self.forward_kinematics = PyBulletForwardKinematics(self.client)
        self.inverse_kinematics = PyBulletInverseKinematics(self.client)
