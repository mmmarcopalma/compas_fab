"""
.. _compas_fabrication.fabrication.robots.rfl:

********************************************************************************
compas_fabrication.fabrication.robots.rfl
********************************************************************************

.. module:: compas_fabrication.fabrication.robots.rfl

Package with functionality to run simulations on the RFL (Robotic Fabrication
Lab) using robotic simulation tools like
`v-rep <http://www.coppeliarobotics.com/>`_.

.. autosummary::
    :toctree: generated/

    Robot
    Configuration
    Simulator
    SimulatorXform

"""

from compas_fabrication.fabrication.robots.rfl.simulator import Simulator, SimulationError
from compas_fabrication.fabrication.robots.rfl.robots import Robot, Configuration, SimulatorXform
