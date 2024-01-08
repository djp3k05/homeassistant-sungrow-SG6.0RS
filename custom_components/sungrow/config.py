from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorStateClass
)
from homeassistant.components.sensor import (
    SensorEntityDescription
)
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    ENERGY_KILO_WATT_HOUR,
    PERCENTAGE,
    POWER_WATT,
    DEVICE_CLASS_VOLTAGE
)
from homeassistant.components.sensor import (
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    ENERGY_KILO_WATT_HOUR,
    DEVICE_CLASS_POWER,
    POWER_WATT,
    DEVICE_CLASS_VOLTAGE
)


from .const import (
    SUNGROW_phase_a_voltage,
    SUNGROW_work_state_1,
    SUNGROW_MPPT1_VOLTAGE,
    SUNGROW_MPPT1_CURRENT,
    SUNGROW_MPPT2_VOLTAGE,
    SUNGROW_MPPT2_CURRENT,
    SUNGROW_internal_temperature,
    SUNGROW_total_reactive_power,
    SUNGROW_array_insulation_resistance,
    SUNGROW_work_state_2,
    SUNGROW_total_power_yields,
    SUNGROW_negative_voltage_to_the_ground,
    SUNGROW_bus_voltage,
    SUNGROW_grid_frequency,
    SUNGROW_pid_work_state,
    SUNGROW_pid_alarm_code,
    SUNGROW_power_meter,
    SUNGROW_string_1_current,
    SUNGROW_string_2_current,
    SUNGROW_pid_recovery,
    SUNGROW_total_running_time,
    SUNGROW_total_apparent_power,
    SUNGROW_DAILY_POWER_YIELDS,
    SUNGROW_ENERGY_GENERATION,
    SUNGROW_ARRAY1_ENERGY_GENERATION,
    SUNGROW_ARRAY2_ENERGY_GENERATION,
    SUNGROW_POWER_EXPORT_TO_GRID,
    SUNGROW_POWER_IMPORT_FROM_GRID,
    SUNGROW_METER_POWER,
    SUNGROW_TOTAL_ACTIVE_POWER,
    SUNGROW_LOAD_POWER,
    SUNGROW_EXPORT_POWER,
)


@dataclass
class SungrowInverterSensorEntityDescription(SensorEntityDescription):
    register: str = None
    device_id: str = None
    device_model: str = None
    _original_name: str = None

    @property
    def original_name(self):
        """Capture original name since we will mutate name later"""
        if not self._original_name:
            self._original_name = self.name
        return self._original_name


SENSOR_TYPES = (
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_total_apparent_power,
        register=SUNGROW_total_apparent_power,
        name="Total Apparent Power",
    ), 
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_total_running_time,
        register=SUNGROW_total_running_time,
        name="Total Running Time",
    ),  
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_pid_recovery,
        register=SUNGROW_pid_recovery,
        name="Pid Recovery",
    ),  
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_string_1_current,
        register=SUNGROW_string_1_current,
        name="String 1 Current",
    ),    
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_string_2_current,
        register=SUNGROW_string_2_current,
        name="String 2 Current",
    ),    
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_power_meter,
        register=SUNGROW_power_meter,
        name="Power Meter",
    ),    
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_pid_alarm_code,
        register=SUNGROW_pid_alarm_code,
        name="Pid Alarm Code",
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_pid_work_state,
        register=SUNGROW_pid_work_state,
        name="Pid Work State",
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_grid_frequency,
        register=SUNGROW_grid_frequency,
        name="Grid Frequency",
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_bus_voltage,
        register=SUNGROW_bus_voltage,
        name="Bus Voltage",
    ),       
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_negative_voltage_to_the_ground,
        register=SUNGROW_negative_voltage_to_the_ground,
        name="Negative Voltage to the Ground",
    ),     
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_total_power_yields,
        register=SUNGROW_total_power_yields,
        name="TotaT Power Yields",
    ),        
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_work_state_2,
        register=SUNGROW_work_state_2,
        name="Work State 2",
    ),     
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_array_insulation_resistance,
        register=SUNGROW_array_insulation_resistance,
        name="Array Insulation Resistance",
    ),  
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_total_reactive_power,
        register=SUNGROW_total_reactive_power,
        name="Total Reactive Power",
    ),    
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_internal_temperature,
        register=SUNGROW_internal_temperature,
        name="Temperature",
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_phase_a_voltage,
        register=SUNGROW_phase_a_voltage,
        name="Phase A Voltage",
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_work_state_1,
        register=SUNGROW_work_state_1,
        name="Work State",
    ),    
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_MPPT1_VOLTAGE,
        register=SUNGROW_MPPT1_VOLTAGE,
        name="MPPT1 VOLTAGE",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_MPPT1_CURRENT,
        register=SUNGROW_MPPT1_CURRENT,
        name="MPPT1 Current",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_MPPT2_VOLTAGE,
        register=SUNGROW_MPPT2_VOLTAGE,
        name="MPPT2 VOLTAGE",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_MPPT2_CURRENT,
        register=SUNGROW_MPPT2_CURRENT,
        name="MPPT2 Current",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),       
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_ENERGY_GENERATION,
        register=SUNGROW_ENERGY_GENERATION,
        name="Current PV Power Generation",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_ARRAY1_ENERGY_GENERATION,
        register=SUNGROW_ARRAY1_ENERGY_GENERATION,
        name="Current PV Array 1 Power Generation",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_ARRAY2_ENERGY_GENERATION,
        register=SUNGROW_ARRAY2_ENERGY_GENERATION,
        name="Current PV Array 2 Power Generation",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_LOAD_POWER,
        register=SUNGROW_LOAD_POWER,
        name="Current Load Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_EXPORT_POWER,
        register=SUNGROW_EXPORT_POWER,
        name="Current Export Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_DAILY_POWER_YIELDS,
        register=SUNGROW_DAILY_POWER_YIELDS,
        name="Daily Energy Yields",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_METER_POWER,
        register=SUNGROW_METER_POWER,
        name="Current Meter Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_TOTAL_ACTIVE_POWER,
        register=SUNGROW_TOTAL_ACTIVE_POWER,
        name="Current Active Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_POWER_EXPORT_TO_GRID,
        register=SUNGROW_POWER_EXPORT_TO_GRID,
        name="Current Power Exported to Grid",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SungrowInverterSensorEntityDescription(
        key=SUNGROW_POWER_IMPORT_FROM_GRID,
        register=SUNGROW_POWER_IMPORT_FROM_GRID,
        name="Current Power Imported from Grid",
        native_unit_of_measurement=POWER_WATT,
        device_class=DEVICE_CLASS_POWER,
        state_class=SensorStateClass.MEASUREMENT,
    )
)
