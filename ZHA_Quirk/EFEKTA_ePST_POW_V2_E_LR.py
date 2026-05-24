
from typing import Final
from enum import IntEnum

from zigpy.profiles import zha
from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import (
    QuirkBuilder,
    SensorDeviceClass,
    SensorStateClass,
    EntityType,
    EntityPlatform,
)
from zigpy.quirks.v2.homeassistant.number import NumberDeviceClass
import zigpy.types as t
from zigpy.zcl import ClusterType
from zigpy.zcl.foundation import ZCLAttributeDef
from zigpy.zcl.clusters.general import Basic, PowerConfiguration
from zigpy.zcl.clusters.measurement import (
    TemperatureMeasurement,
    PressureMeasurement,
)
from zigpy.quirks.v2.homeassistant import (
    UnitOfTime,
    UnitOfTemperature,
    UnitOfPressure,
)

EFEKTA = "EfektaLab"

class TxRadioPowerEnum(IntEnum):
    PLUS_4 = 4
    PLUS_19 = 19
    
class InvertEnum(IntEnum):
    BW = 0
    WB = 1
    
class FastModeEnum(IntEnum):
    FAST = 0
    ULTRA_FAST = 1
    
class SensorTypeEnum(IntEnum):
    BAR_1 = 1
    BAR_5 = 5
    BAR_6 = 6
    BAR_10 = 10
    BAR_12 = 12
    BAR_40 = 40

class PowerCfg(PowerConfiguration, CustomCluster):
    class AttributeDefs(PowerConfiguration.AttributeDefs):
        reading_interval: Final = ZCLAttributeDef(id=0x0201, type=t.uint16_t, access="rw")
        comparison_previous_data: Final = ZCLAttributeDef(id=0x0205, type=t.Bool, access="rw")
        tx_radio_power: Final = ZCLAttributeDef(id=0x0236, type=t.int8s, access="rw")
        invert: Final = ZCLAttributeDef(id=0xF004, type=t.uint8_t, access="rw")
        fastmode: Final = ZCLAttributeDef(id=0xF005, type=t.uint8_t, access="rw")

class TempMeasurement(TemperatureMeasurement, CustomCluster):
    class AttributeDefs(TemperatureMeasurement.AttributeDefs):
        temperature_offset: Final = ZCLAttributeDef(id=0x0210, type=t.int16s, access="rw")
        
class PressMeasurement(PressureMeasurement, CustomCluster):
    class AttributeDefs(PressureMeasurement.AttributeDefs):
        sensor_type: Final = ZCLAttributeDef(id=0x0280, type=t.uint8_t, access="rw")
        pressure_offset: Final = ZCLAttributeDef(id=0x0210, type=t.int16s, access="rw")
        
(
    QuirkBuilder(EFEKTA, "EFEKTA_ePST_POW_V2_E_LR")
    .replaces_endpoint(1, device_type=zha.DeviceType.PRESSURE_SENSOR)
    .replaces_endpoint(2, device_type=zha.DeviceType.TEMPERATURE_SENSOR)
    .replaces(Basic, endpoint_id=1)
    .replaces(PowerCfg, endpoint_id=1)
    .replaces(PressMeasurement, endpoint_id=1)
    .replaces(TempMeasurement, endpoint_id=2)
    .skip_configuration(True)
    .sensor(
        "mains_voltage",
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="mains_voltage",
        fallback_name="Mains voltage",
        unique_id_suffix="mains_voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        unit="V",
        multiplier=0.1, 
    )
    .number(
        PressMeasurement.AttributeDefs.pressure_offset.name,
        PressMeasurement.cluster_id,
        endpoint_id=1,
        translation_key="pressure_offset",
        fallback_name="Pressure offset",
        unique_id_suffix="pressure_offset",
        min_value=-100,
        max_value=100,
        step=1,
        device_class=NumberDeviceClass.PRESSURE,
        unit=UnitOfPressure.HPA,
        mode="box",
    )
    .number(
        TempMeasurement.AttributeDefs.temperature_offset.name,
        TempMeasurement.cluster_id,
        endpoint_id=2,
        translation_key="temperature_offset",
        fallback_name="Temperature offset",
        unique_id_suffix="temperature_offset",
        min_value=-50,
        max_value=50,
        step=0.1,
        multiplier=0.1,
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        mode="box",
    )
    .number(
        PowerCfg.AttributeDefs.reading_interval.name,
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="reading_interval",
        fallback_name="Reading interval",
        unique_id_suffix="reading_interval",
        min_value=5,
        max_value=300,
        step=1,
        device_class=NumberDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
    )
    .enum(
        PressMeasurement.AttributeDefs.sensor_type.name,
        SensorTypeEnum,
        PressMeasurement.cluster_id,
        endpoint_id=1,
        translation_key="sensor_type",
        fallback_name="Set sensor type",
        unique_id_suffix="sensor_type",
        entity_type=EntityType.CONFIG,
        entity_platform=EntityPlatform.SELECT,
    )
    .enum(
        PowerCfg.AttributeDefs.tx_radio_power.name,
        TxRadioPowerEnum,
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="tx_radio_power",
        fallback_name="Set TX Radio Power",
        unique_id_suffix="tx_radio_power",
        entity_type=EntityType.CONFIG,
        entity_platform=EntityPlatform.SELECT,
    )
    .enum(
        PowerCfg.AttributeDefs.invert.name,
        InvertEnum,
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="invert",
        fallback_name="Invert display color",
        unique_id_suffix="invert",
        entity_type=EntityType.CONFIG,
        entity_platform=EntityPlatform.SELECT,
    )
    .enum(
        PowerCfg.AttributeDefs.fastmode.name,
        FastModeEnum,
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="fastmode",
        fallback_name="Display refresh mode",
        unique_id_suffix="fastmode",
        entity_type=EntityType.CONFIG,
        entity_platform=EntityPlatform.SELECT,
    )
    .switch(
        PowerCfg.AttributeDefs.comparison_previous_data.name,
        PowerCfg.cluster_id,
        endpoint_id=1,
        translation_key="comparison_previous_data",
        fallback_name="Enable control of comparison with previous data",
        unique_id_suffix="comparison_previous_data",
    )
    
    .add_to_registry()
)