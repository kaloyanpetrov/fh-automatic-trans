import struct


class FHDataPacket:
    fh4_format = '<iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiiifffffffffffffffffHBBBBBBbbb'
    fh4_props = [
        'is_race_on', 'timestamp_ms',
        'engine_max_rpm', 'engine_idle_rpm', 'current_engine_rpm',
        'acceleration_x', 'acceleration_y', 'acceleration_z',
        'velocity_x', 'velocity_y', 'velocity_z',
        'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z',
        'yaw', 'pitch', 'roll',
        'norm_suspension_travel_FL', 'norm_suspension_travel_FR',
        'norm_suspension_travel_RL', 'norm_suspension_travel_RR',
        'tire_slip_ratio_FL', 'tire_slip_ratio_FR',
        'tire_slip_ratio_RL', 'tire_slip_ratio_RR',
        'wheel_rotation_speed_FL', 'wheel_rotation_speed_FR',
        'wheel_rotation_speed_RL', 'wheel_rotation_speed_RR',
        'wheel_on_rumble_strip_FL', 'wheel_on_rumble_strip_FR',
        'wheel_on_rumble_strip_RL', 'wheel_on_rumble_strip_RR',
        'wheel_in_puddle_FL', 'wheel_in_puddle_FR',
        'wheel_in_puddle_RL', 'wheel_in_puddle_RR',
        'surface_rumble_FL', 'surface_rumble_FR',
        'surface_rumble_RL', 'surface_rumble_RR',
        'tire_slip_angle_FL', 'tire_slip_angle_FR',
        'tire_slip_angle_RL', 'tire_slip_angle_RR',
        'tire_combined_slip_FL', 'tire_combined_slip_FR',
        'tire_combined_slip_RL', 'tire_combined_slip_RR',
        'suspension_travel_meters_FL', 'suspension_travel_meters_FR',
        'suspension_travel_meters_RL', 'suspension_travel_meters_RR',
        'car_ordinal', 'car_class', 'car_performance_index',
        'drivetrain_type', 'num_cylinders',
        'position_x', 'position_y', 'position_z',
        'speed', 'power', 'torque',
        'tire_temp_FL', 'tire_temp_FR',
        'tire_temp_RL', 'tire_temp_RR',
        'boost', 'fuel', 'dist_traveled',
        'best_lap_time', 'last_lap_time',
        'cur_lap_time', 'cur_race_time',
        'lap_no', 'race_pos',
        'accel', 'brake', 'clutch', 'handbrake',
        'gear', 'steer',
        'norm_driving_line', 'norm_ai_brake_diff'
    ]

    def __init__(self, data):
        self.packet_format = 'fh4'      # might delete later
        patched_data = data[:232] + data[244:323]
        for prop_name, prop_value in zip(self.fh4_props, struct.unpack(self.fh4_format, patched_data)):
            setattr(self, prop_name, prop_value)

    def to_list(self, attributes):
        if attributes:
            return [getattr(self, a) for a in attributes]
        return [getattr(self, prop_name) for prop_name in self.fh4_props]

    @staticmethod
    def get_props():
        return 'fh4'

    def get_format(self):
        return self.packet_format

    # Return a tab-separated string with the names of all properties in the order defined in the data packet.
    def get_tsv_header(self):
        return '\t'.join(self.fh4_props)

    def to_tsv(self):
        """
        Return a tab-separated values string with all data in the given order.
        All floating point numbers are defined as such to allow for changing
        the number of significant digits if desired.
        """
        return '{0.is_race_on}' \
               '\t{0.timestamp_ms}' \
               '\t{0.engine_max_rpm:f}' \
               '\t{0.engine_idle_rpm:f}' \
               '\t{0.current_engine_rpm:f}' \
               '\t{0.acceleration_x:f}' \
               '\t{0.acceleration_y:f}' \
               '\t{0.acceleration_z:f}' \
               '\t{0.velocity_x:f}' \
               '\t{0.velocity_y:f}' \
               '\t{0.velocity_z:f}' \
               '\t{0.angular_velocity_x:f}' \
               '\t{0.angular_velocity_y:f}' \
               '\t{0.angular_velocity_z:f}' \
               '\t{0.yaw:f}\t{0.pitch:f}' \
               '\t{0.roll:f}' \
               '\t{0.norm_suspension_travel_FL:f}' \
               '\t{0.norm_suspension_travel_FR:f}' \
               '\t{0.norm_suspension_travel_RL:f}' \
               '\t{0.norm_suspension_travel_RR:f}' \
               '\t{0.tire_slip_ratio_FL:f}' \
               '\t{0.tire_slip_ratio_FR:f}' \
               '\t{0.tire_slip_ratio_RL:f}' \
               '\t{0.tire_slip_ratio_RR:f}' \
               '\t{0.wheel_rotation_speed_FL:f}' \
               '\t{0.wheel_rotation_speed_FR:f}' \
               '\t{0.wheel_rotation_speed_RL:f}' \
               '\t{0.wheel_rotation_speed_RR:f}' \
               '\t{0.wheel_on_rumble_strip_FL:f}' \
               '\t{0.wheel_on_rumble_strip_FR:f}' \
               '\t{0.wheel_on_rumble_strip_RL:f}' \
               '\t{0.wheel_on_rumble_strip_RR:f}' \
               '\t{0.wheel_in_puddle_FL:f}' \
               '\t{0.wheel_in_puddle_FR:f}' \
               '\t{0.wheel_in_puddle_RL:f}' \
               '\t{0.wheel_in_puddle_RR:f}' \
               '\t{0.surface_rumble_FL:f}' \
               '\t{0.surface_rumble_FR:f}' \
               '\t{0.surface_rumble_RL:f}' \
               '\t{0.surface_rumble_RR:f}' \
               '\t{0.tire_slip_angle_FL:f}' \
               '\t{0.tire_slip_angle_FR:f}' \
               '\t{0.tire_slip_angle_RL:f}' \
               '\t{0.tire_slip_angle_RR:f}' \
               '\t{0.tire_combined_slip_FL:f}' \
               '\t{0.tire_combined_slip_FR:f}' \
               '\t{0.tire_combined_slip_RL:f}' \
               '\t{0.tire_combined_slip_RR:f}' \
               '\t{0.suspension_travel_meters_FL:f}' \
               '\t{0.suspension_travel_meters_FR:f}' \
               '\t{0.suspension_travel_meters_RL:f}' \
               '\t{0.suspension_travel_meters_RR:f}' \
               '\t{0.car_ordinal}\t{0.car_class}' \
               '\t{0.car_performance_index}' \
               '\t{0.drivetrain_type}' \
               '\t{0.num_cylinders}' \
               '\t{0.position_x}' \
               '\t{0.position_y}' \
               '\t{0.position_z}' \
               '\t{0.speed}' \
               '\t{0.power}' \
               '\t{0.torque}' \
               '\t{0.tire_temp_FL}' \
               '\t{0.tire_temp_FR}' \
               '\t{0.tire_temp_RL}' \
               '\t{0.tire_temp_RR}' \
               '\t{0.boost}' \
               '\t{0.fuel}' \
               '\t{0.dist_traveled}' \
               '\t{0.best_lap}' \
               '\t{0.last_lap}' \
               '\t{0.cur_lap}' \
               '\t{0.cur_race_time}' \
               '\t{0.lap_no}' \
               '\t{0.race_pos}' \
               '\t{0.accel}' \
               '\t{0.brake}' \
               '\t{0.clutch}' \
               '\t{0.handbrake}' \
               '\t{0.gear}' \
               '\t{0.steer}' \
               '\t{0.norm_driving_line}' \
               '\t{0.norm_ai_brake_diff}'.format(self)
