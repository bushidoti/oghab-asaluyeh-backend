from django.db import models
from django.core.validators import MaxValueValidator


class AutoIncrementProperty(models.Model):
    airport_equipment_01 = models.BigIntegerField(validators=[MaxValueValidator(10101999)], blank=True, null=True)
    safety_equipment_01 = models.BigIntegerField(validators=[MaxValueValidator(10102999)], blank=True, null=True)
    airport_vehicle_01 = models.BigIntegerField(validators=[MaxValueValidator(10103999)], blank=True, null=True)
    office_vehicle_01 = models.BigIntegerField(validators=[MaxValueValidator(10104999)], blank=True, null=True)
    airport_furniture_01 = models.BigIntegerField(validators=[MaxValueValidator(10105999)], blank=True, null=True)
    office_furniture_01 = models.BigIntegerField(validators=[MaxValueValidator(10106999)], blank=True, null=True)
    electronic_furniture_01 = models.BigIntegerField(validators=[MaxValueValidator(10107999)], blank=True, null=True)
    facility_furniture_01 = models.BigIntegerField(validators=[MaxValueValidator(10108999)], blank=True, null=True)
    digital_furniture_01 = models.BigIntegerField(validators=[MaxValueValidator(10109999)], blank=True, null=True)
    none_industrial_tools_01 = models.BigIntegerField(validators=[MaxValueValidator(101010999)], blank=True, null=True)
    industrial_tools_01 = models.BigIntegerField(validators=[MaxValueValidator(101011999)], blank=True, null=True)
    benefit_01 = models.BigIntegerField(validators=[MaxValueValidator(101012999)], blank=True, null=True)
    support_item_01 = models.BigIntegerField(validators=[MaxValueValidator(101013999)], blank=True, null=True)
    airplane_01 = models.BigIntegerField(validators=[MaxValueValidator(101014999)], blank=True, null=True)
    airport_equipment_02 = models.BigIntegerField(validators=[MaxValueValidator(10201999)], blank=True, null=True)
    safety_equipment_02 = models.BigIntegerField(validators=[MaxValueValidator(10202999)], blank=True, null=True)
    airport_vehicle_02 = models.BigIntegerField(validators=[MaxValueValidator(10203999)], blank=True, null=True)
    office_vehicle_02 = models.BigIntegerField(validators=[MaxValueValidator(10204999)], blank=True, null=True)
    airport_furniture_02 = models.BigIntegerField(validators=[MaxValueValidator(10205999)], blank=True, null=True)
    office_furniture_02 = models.BigIntegerField(validators=[MaxValueValidator(10206999)], blank=True, null=True)
    electronic_furniture_02 = models.BigIntegerField(validators=[MaxValueValidator(10207999)], blank=True, null=True)
    facility_furniture_02 = models.BigIntegerField(validators=[MaxValueValidator(10208999)], blank=True, null=True)
    digital_furniture_02 = models.BigIntegerField(validators=[MaxValueValidator(10209999)], blank=True, null=True)
    none_industrial_tools_02 = models.BigIntegerField(validators=[MaxValueValidator(102010999)], blank=True, null=True)
    industrial_tools_02 = models.BigIntegerField(validators=[MaxValueValidator(102011999)], blank=True, null=True)
    benefit_02 = models.BigIntegerField(validators=[MaxValueValidator(102012999)], blank=True, null=True)
    support_item_02 = models.BigIntegerField(validators=[MaxValueValidator(102013999)], blank=True, null=True)
    airplane_02 = models.BigIntegerField(validators=[MaxValueValidator(102014999)], blank=True, null=True)
    airport_equipment_03 = models.BigIntegerField(validators=[MaxValueValidator(10301999)], blank=True, null=True)
    safety_equipment_03 = models.BigIntegerField(validators=[MaxValueValidator(10302999)], blank=True, null=True)
    airport_vehicle_03 = models.BigIntegerField(validators=[MaxValueValidator(10303999)], blank=True, null=True)
    office_vehicle_03 = models.BigIntegerField(validators=[MaxValueValidator(10304999)], blank=True, null=True)
    airport_furniture_03 = models.BigIntegerField(validators=[MaxValueValidator(10305999)], blank=True, null=True)
    office_furniture_03 = models.BigIntegerField(validators=[MaxValueValidator(10306999)], blank=True, null=True)
    electronic_furniture_03 = models.BigIntegerField(validators=[MaxValueValidator(10307999)], blank=True, null=True)
    facility_furniture_03 = models.BigIntegerField(validators=[MaxValueValidator(10308999)], blank=True, null=True)
    digital_furniture_03 = models.BigIntegerField(validators=[MaxValueValidator(10309999)], blank=True, null=True)
    none_industrial_tools_03 = models.BigIntegerField(validators=[MaxValueValidator(103010999)], blank=True, null=True)
    industrial_tools_03 = models.BigIntegerField(validators=[MaxValueValidator(103011999)], blank=True, null=True)
    benefit_03 = models.BigIntegerField(validators=[MaxValueValidator(103012999)], blank=True, null=True)
    support_item_03 = models.BigIntegerField(validators=[MaxValueValidator(103013999)], blank=True, null=True)
    airplane_03 = models.BigIntegerField(validators=[MaxValueValidator(103014999)], blank=True, null=True)
    airport_equipment_04 = models.BigIntegerField(validators=[MaxValueValidator(10401999)], blank=True, null=True)
    safety_equipment_04 = models.BigIntegerField(validators=[MaxValueValidator(10402999)], blank=True, null=True)
    airport_vehicle_04 = models.BigIntegerField(validators=[MaxValueValidator(10403999)], blank=True, null=True)
    office_vehicle_04 = models.BigIntegerField(validators=[MaxValueValidator(10404999)], blank=True, null=True)
    airport_furniture_04 = models.BigIntegerField(validators=[MaxValueValidator(10405999)], blank=True, null=True)
    office_furniture_04 = models.BigIntegerField(validators=[MaxValueValidator(10406999)], blank=True, null=True)
    electronic_furniture_04 = models.BigIntegerField(validators=[MaxValueValidator(10407999)], blank=True, null=True)
    facility_furniture_04 = models.BigIntegerField(validators=[MaxValueValidator(10408999)], blank=True, null=True)
    digital_furniture_04 = models.BigIntegerField(validators=[MaxValueValidator(10409999)], blank=True, null=True)
    none_industrial_tools_04 = models.BigIntegerField(validators=[MaxValueValidator(104010999)], blank=True, null=True)
    industrial_tools_04 = models.BigIntegerField(validators=[MaxValueValidator(104011999)], blank=True, null=True)
    benefit_04 = models.BigIntegerField(validators=[MaxValueValidator(104012999)], blank=True, null=True)
    support_item_04 = models.BigIntegerField(validators=[MaxValueValidator(104013999)], blank=True, null=True)
    airplane_04 = models.BigIntegerField(validators=[MaxValueValidator(104014999)], blank=True, null=True)
    airport_equipment_05 = models.BigIntegerField(validators=[MaxValueValidator(10501999)], blank=True, null=True)
    safety_equipment_05 = models.BigIntegerField(validators=[MaxValueValidator(10502999)], blank=True, null=True)
    airport_vehicle_05 = models.BigIntegerField(validators=[MaxValueValidator(10503999)], blank=True, null=True)
    office_vehicle_05 = models.BigIntegerField(validators=[MaxValueValidator(10504999)], blank=True, null=True)
    airport_furniture_05 = models.BigIntegerField(validators=[MaxValueValidator(10505999)], blank=True, null=True)
    office_furniture_05 = models.BigIntegerField(validators=[MaxValueValidator(10506999)], blank=True, null=True)
    electronic_furniture_05 = models.BigIntegerField(validators=[MaxValueValidator(10507999)], blank=True, null=True)
    facility_furniture_05 = models.BigIntegerField(validators=[MaxValueValidator(10508999)], blank=True, null=True)
    digital_furniture_05 = models.BigIntegerField(validators=[MaxValueValidator(10509999)], blank=True, null=True)
    none_industrial_tools_05 = models.BigIntegerField(validators=[MaxValueValidator(105010999)], blank=True, null=True)
    industrial_tools_05 = models.BigIntegerField(validators=[MaxValueValidator(105011999)], blank=True, null=True)
    benefit_05 = models.BigIntegerField(validators=[MaxValueValidator(105012999)], blank=True, null=True)
    support_item_05 = models.BigIntegerField(validators=[MaxValueValidator(105013999)], blank=True, null=True)
    airplane_05 = models.BigIntegerField(validators=[MaxValueValidator(105014999)], blank=True, null=True)
    airport_equipment_06 = models.BigIntegerField(validators=[MaxValueValidator(10601999)], blank=True, null=True)
    safety_equipment_06 = models.BigIntegerField(validators=[MaxValueValidator(10602999)], blank=True, null=True)
    airport_vehicle_06 = models.BigIntegerField(validators=[MaxValueValidator(10603999)], blank=True, null=True)
    office_vehicle_06 = models.BigIntegerField(validators=[MaxValueValidator(10604999)], blank=True, null=True)
    airport_furniture_06 = models.BigIntegerField(validators=[MaxValueValidator(10605999)], blank=True, null=True)
    office_furniture_06 = models.BigIntegerField(validators=[MaxValueValidator(10606999)], blank=True, null=True)
    electronic_furniture_06 = models.BigIntegerField(validators=[MaxValueValidator(10607999)], blank=True, null=True)
    facility_furniture_06 = models.BigIntegerField(validators=[MaxValueValidator(10608999)], blank=True, null=True)
    digital_furniture_06 = models.BigIntegerField(validators=[MaxValueValidator(10609999)], blank=True, null=True)
    none_industrial_tools_06 = models.BigIntegerField(validators=[MaxValueValidator(106010999)], blank=True, null=True)
    industrial_tools_06 = models.BigIntegerField(validators=[MaxValueValidator(106011999)], blank=True, null=True)
    benefit_06 = models.BigIntegerField(validators=[MaxValueValidator(106012999)], blank=True, null=True)
    support_item_06 = models.BigIntegerField(validators=[MaxValueValidator(106013999)], blank=True, null=True)
    airplane_06 = models.BigIntegerField(validators=[MaxValueValidator(106014999)], blank=True, null=True)
    airport_equipment_07 = models.BigIntegerField(validators=[MaxValueValidator(10701999)], blank=True, null=True)
    safety_equipment_07 = models.BigIntegerField(validators=[MaxValueValidator(10702999)], blank=True, null=True)
    airport_vehicle_07 = models.BigIntegerField(validators=[MaxValueValidator(10703999)], blank=True, null=True)
    office_vehicle_07 = models.BigIntegerField(validators=[MaxValueValidator(10704999)], blank=True, null=True)
    airport_furniture_07 = models.BigIntegerField(validators=[MaxValueValidator(10705999)], blank=True, null=True)
    office_furniture_07 = models.BigIntegerField(validators=[MaxValueValidator(10706999)], blank=True, null=True)
    electronic_furniture_07 = models.BigIntegerField(validators=[MaxValueValidator(10707999)], blank=True, null=True)
    facility_furniture_07 = models.BigIntegerField(validators=[MaxValueValidator(10708999)], blank=True, null=True)
    digital_furniture_07 = models.BigIntegerField(validators=[MaxValueValidator(10709999)], blank=True, null=True)
    none_industrial_tools_07 = models.BigIntegerField(validators=[MaxValueValidator(107010999)], blank=True, null=True)
    industrial_tools_07 = models.BigIntegerField(validators=[MaxValueValidator(107011999)], blank=True, null=True)
    benefit_07 = models.BigIntegerField(validators=[MaxValueValidator(107012999)], blank=True, null=True)
    support_item_07 = models.BigIntegerField(validators=[MaxValueValidator(107013999)], blank=True, null=True)
    airplane_07 = models.BigIntegerField(validators=[MaxValueValidator(107014999)], blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد ثبت اموال"

class AirportEquipment(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "تجهیزات فرودگاهی"


class RepairedAirportEquipment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    airport_equipment = models.ForeignKey(AirportEquipment, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات تجهیزات فرودگاهی"


class SafetyEquipment(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    use_for = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "تجهیزات ایمنی"


class RepairedSafetyEquipment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    safety_equipment = models.ForeignKey(SafetyEquipment, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات تجهیزات ایمنی"


class AirportVehicle(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    plate1 = models.CharField(max_length=50, blank=True, null=True)
    plate2 = models.CharField(max_length=50, blank=True, null=True)
    plate3 = models.CharField(max_length=50, blank=True, null=True)
    plate4 = models.CharField(max_length=50, blank=True, null=True)
    motor = models.CharField(max_length=50, blank=True, null=True)
    chassis = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "خودرو فرودگاهی"

class RepairedAirportVehicle(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    airport_vehicle = models.ForeignKey(AirportVehicle, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات خودرو فرودگاهی"


class OfficeVehicle(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    plate1 = models.CharField(max_length=50, blank=True, null=True)
    plate2 = models.CharField(max_length=50, blank=True, null=True)
    plate3 = models.CharField(max_length=50, blank=True, null=True)
    plate4 = models.CharField(max_length=50, blank=True, null=True)
    motor = models.CharField(max_length=50, blank=True, null=True)
    chassis = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "خودرو اداری"

class RepairedOfficeVehicle(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    office_vehicle = models.ForeignKey(OfficeVehicle, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات خودرو اداری"


class AirportFurniture(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اثاث فرودگاهی"

class RepairedAirportFurniture(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    airport_furniture = models.ForeignKey(AirportFurniture, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اثاث فرودگاهی"


class Airplane(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    plate1 = models.CharField(max_length=50, blank=True, null=True)
    plate2 = models.CharField(max_length=50, blank=True, null=True)
    plate3 = models.CharField(max_length=50, blank=True, null=True)
    plate4 = models.CharField(max_length=50, blank=True, null=True)
    motor = models.CharField(max_length=50, blank=True, null=True)
    chassis = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "هواپیما"


class RepairedAirplane(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    kilometer = models.BigIntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    year_changed = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات هواپیما"


class OfficeFurniture(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_made = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    using_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اثاث اداری"


class RepairedOfficeFurniture(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    office_furniture = models.ForeignKey(OfficeFurniture, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اثاث اداری"

class ElectronicFurniture(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اثاث الکترونیکی"

class RepairedElectronicFurniture(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    electronic_furniture = models.ForeignKey(ElectronicFurniture, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اثاث الکترونیکی"


class FacilityFurniture(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اثاث تاسیساتی"


class RepairedFacilityFurniture(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    facility_furniture = models.ForeignKey(FacilityFurniture, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اثاث تاسیساتی"

class DigitalFurniture(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    phone_feature = models.CharField(max_length=50, blank=True, null=True)
    cpu = models.CharField(max_length=50, blank=True, null=True)
    motherboard = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    power = models.CharField(max_length=50, blank=True, null=True)
    hdd = models.CharField(max_length=50, blank=True, null=True)
    case = models.CharField(max_length=50, blank=True, null=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    install_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    type_furniture = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اقلام دیجیتال"


class RepairedDigitalFurniture(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    repaired_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    digital_furniture = models.ForeignKey(DigitalFurniture, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اقلام دیجیتال"


class NoneIndustrialTool(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    using_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اقلام غیر صنعتی"


class IndustrialTool(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year_buy = models.IntegerField(blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    using_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    repaired_status = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name_plural = "اقلام صنعتی"


class RepairedIndustrialTool(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    industrial_tool = models.ForeignKey(IndustrialTool, on_delete=models.CASCADE)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "تعمیرات اقلام صنعتی"


class Benefit(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    number_type = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    using_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "امتیازات"


class SupportItem(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    property_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    type_item = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    dst_inventory = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    using_location = models.CharField(max_length=50, blank=True, null=True)
    type_register = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    movement_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    sign_received = models.TextField(max_length=500, blank=True, null=True)
    last_handling_result = models.TextField(max_length=500, blank=True, null=True)
    last_handling_date = models.CharField(max_length=50, blank=True, null=True)
    yearly_handling = models.CharField(max_length=4, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.BigIntegerField(blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    canceled_describe = models.TextField(blank=True, null=True)
    cancel_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "اقلام پشتیبانی"


class Factors(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    systemID = models.CharField(max_length=50, blank=True, null=True)
    factor = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "فاکتور ها"

class AutoIncrementFactor(models.Model):
    systemID_01 = models.BigIntegerField(blank=True, null=True)
    systemID_02 = models.BigIntegerField(blank=True, null=True)
    systemID_03 = models.BigIntegerField(blank=True, null=True)
    systemID_04 = models.BigIntegerField(blank=True, null=True)
    systemID_05 = models.BigIntegerField(blank=True, null=True)
    systemID_06 = models.BigIntegerField(blank=True, null=True)
    systemID_07 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "شمارنده کد فاکتور"
