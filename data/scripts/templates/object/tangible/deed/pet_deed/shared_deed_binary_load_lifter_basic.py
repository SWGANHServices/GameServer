#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Tangible()

	result.template = "object/tangible/deed/pet_deed/shared_deed_binary_load_lifter_basic.iff"
	result.attribute_template_id = 2
	result.stfName("deed","binary_load_lifter_basic_deed")		
	
	#### BEGIN MODIFICATIONS ####
	result.setStringAttribute("radial_filename", "radials/deed_datapad.py")
	result.setStringAttribute("deed_pcd", "object/intangible/pet/shared_cll8_binary_load_lifter.iff")
	result.setStringAttribute("deed_mobile", "object/mobile/shared_cll8_binary_load_lifter.iff")
	####  END MODIFICATIONS  ####
	
	return result