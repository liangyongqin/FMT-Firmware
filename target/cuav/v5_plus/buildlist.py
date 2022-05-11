# Build Lists
# Modify this file to control which files/modules should be built

DRIVERS = [
    'imu/icm20689.c',
    'imu/bmi055.c',
    'mag/ist8310.c',
    'barometer/ms5611.c',
    'gps/gps_m8n.c',
    'rgb_led/ncp5623c.c',
]

DRIVERS_CPPPATH = []

HAL = [
    'pin/*.c',
    'serial/*.c',
    'systick/*.c',
    'sd/*.c',
    'usb/usbd_cdc.c',
    'spi/spi_core.c',
    'spi/spi_dev.c',
    'i2c/*.c',
    'gyro/*.c',
    'accel/*.c',
    'mag/*.c',
    'barometer/*.c',
    'fmtio_dev/*.c',
    'motor/*.c',
    'actuator/*.c',
    'rc/*.c',
    'gps/*.c',
    'adc/*.c',
]

HAL_CPPPATH = []

MODULES = [
    'calibration/*.c',
    'console/*.c',
    'system/*.c',
    'ipc/*.c',
    'syscmd/*.c',
    'file_manager/*.c',
    'ftp/*.c',
    "log/*.c",
    "param/*.c",
    'utils/*.c',
    'mavproxy/*.c',
    'sensor/*.c',
    'sysio/*.c',
    'toml/*.c',
    'workqueue/*.c',
    'math/*.c',
    'filter/*.c',
    'fmtio/*.c',
    'task_manager/*.c',
    'pmu/*.c',
]

MODULES_CPPPATH = [
    'calibration',
]

MODELS = [
    'plant/multicopter/*.c',
    'plant/multicopter/lib/*.c',
    # 'ins/base_ins/*.c',
    # 'ins/base_ins/lib/*.c',
    'ins/px4_ecl/*.c',
    'ins/px4_ecl/lib/*.cpp',
    'ins/px4_ecl/lib/*.c',
    'ins/px4_ecl/ecl/airdata/*.cpp',
    'ins/px4_ecl/ecl/AlphaFilter/*.cpp',
    'ins/px4_ecl/ecl/EKF/*.cpp',
    'ins/px4_ecl/ecl/geo/*.cpp',
    'ins/px4_ecl/ecl/geo_lookup/*.cpp',
    'ins/px4_ecl/ecl/mathlib/*.cpp',
    'ins/px4_ecl/ecl/matrix/*.cpp',
    'fms/base_fms/*.c',
    'fms/base_fms/lib/*.c',
    'control/base_controller/*.c',
    'control/base_controller/lib/*.c',
]

MODELS_CPPPATH = [
    'plant/multicopter/lib',
    # 'ins/base_ins/lib',
    'ins/px4_ecl/lib',
    'ins/px4_ecl/ecl',
    'ins/px4_ecl/ecl/airdata',
    'ins/px4_ecl/ecl/AlphaFilter',
    'ins/px4_ecl/ecl/EKF',
    'ins/px4_ecl/ecl/geo',
    'ins/px4_ecl/ecl/geo_lookup',
    'ins/px4_ecl/ecl/mathlib',
    'ins/px4_ecl/ecl/matrix',
    'fms/base_fms/lib',
    'control/base_controller/lib',
]

TASKS = [
    'simple/*.c',
    'comm/*.c',
    'logger/*.c',
    'fmtio/*.c',
    'status/*.c',
    'vehicle/multicopter/*.c',
]

TASKS_CPPPATH = []

LIBS = [
    'cm_backtrace',
    'mavlink',
]
