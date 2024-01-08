"""Constants for the Sungrow Inverter integration"""

from datetime import timedelta

DOMAIN = 'sungrow'

DEFAULT_NAME = "Sungrow Inverter"
DEFAULT_PORT = 502
DEFAULT_SLAVE = 0x01
DEFAULT_SCAN_INTERVAL = 5
DEFAULT_TIMEOUT = 3

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=5)

SUNGROW_MPPT1_VOLTAGE = "mppt_1_voltage"
SUNGROW_MPPT1_CURRENT = "mppt_1_current"
SUNGROW_MPPT2_VOLTAGE = "mppt_2_voltage"
SUNGROW_MPPT2_CURRENT = "mppt_2_current"
SUNGROW_phase_a_voltage = "phase_a_voltage"
SUNGROW_work_state_1 = "work_state_1"
SUNGROW_internal_temperature = "internal_temperature"
SUNGROW_total_reactive_power = "total_reactive_power"
SUNGROW_array_insulation_resistance = "array_insulation_resistance"
SUNGROW_work_state_2 = "work_state_2"
SUNGROW_total_power_yields = "total_power_yields"
SUNGROW_negative_voltage_to_the_ground = "negative_voltage_to_the_ground"
SUNGROW_bus_voltage = "bus_voltage"
SUNGROW_grid_frequency = "grid_frequency"
SUNGROW_pid_work_state = "pid_work_state"
SUNGROW_pid_alarm_code = "pid_alarm_code"
SUNGROW_power_meter = "power_meter"
SUNGROW_string_1_current = "string_1_current"
SUNGROW_string_2_current = "string_2_current"
SUNGROW_pid_recovery = "pid_recovery"
SUNGROW_total_running_time = "total_running_time"
SUNGROW_total_apparent_power = "total_apparent_power"


# Unit is W
SUNGROW_ENERGY_GENERATION = "energy_generation"

SUNGROW_METER_POWER = "meter_power"
SUNGROW_ARRAY1_ENERGY_GENERATION = "array1_energy_generation"
SUNGROW_ARRAY1_VOLTAGE = "array1_voltage"
SUNGROW_ARRAY1_CURRENT = "array1_current"

SUNGROW_ARRAY2_ENERGY_GENERATION = "array2_energy_generation"
SUNGROW_ARRAY2_VOLTAGE = "array2_voltage"
SUNGROW_ARRAY2_CURRENT = "array2_current"

SUNGROW_LOAD_POWER = "load_power"
SUNGROW_LOAD_POWER_HYBRID = "load_power_hybrid"

SUNGROW_EXPORT_POWER = "export_power"
SUNGROW_EXPORT_POWER_HYBRID = "export_power_hybrid"


SUNGROW_DAILY_PV_ENERGY = "daily_pv_generation"
SUNGROW_TOTAL_PV_ENERGY = "total_pv_generation"

SUNGROW_DAILY_DIRECT_ENERGY_CONSUMPTION = "daily_direct_energy_consumption"
SUNGROW_TOTAL_DIRECT_ENERGY_CONSUMPTION = "total_direct_energy_consumption"

SUNGROW_TOTAL_EXPORT_ENERGY = "total_export_energy"

# TODO these arent real registers. Use daily_pv_export, total_pv_export instead?
SUNGROW_DAILY_EXPORT_ENERGY_FROM_PV = "daily_export_power_from_pv"
SUNGROW_TOTAL_EXPORT_ENERGY_FROM_PV = "total_export_power_from_pv"


SUNGROW_DAILY_POWER_YIELDS =  "daily_power_yields" # kWh

SUNGROW_DAILY_PV_EXPORT = "daily_pv_export"

SUNGROW_TOTAL_ACTIVE_POWER = "total_active_power"

SUNGROW_STATE_FEED_INTO_GRID = "state_feed_into_grid"
SUNGROW_STATE_IMPORT_FROM_GRID = "state_import_from_grid"
SUNGROW_STATE_LOAD_ACTIVE = "state_load_active"

# Synthetic from SunGather
# These are power in W, not energy in kWh
SUNGROW_POWER_EXPORT_TO_GRID = "export_to_grid"
SUNGROW_POWER_IMPORT_FROM_GRID = "import_from_grid"

