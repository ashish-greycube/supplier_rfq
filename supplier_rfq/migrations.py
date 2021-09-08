import frappe
from frappe.modules.import_file import import_file_by_path
from frappe.utils import get_bench_path
import os
from os.path import join

def after_migrate(**args):
	create_custom_fields(**args)
	make_property_setter()

def make_property_setter():
	supplier_rfq_app_folder_path='/apps/supplier_rfq/supplier_rfq/import_records'

	if(not frappe.db.exists('Property Setter','Request for Quotation-main-title_field')):
		fname="property_setter.json"
		import_folder_path="{bench_path}/{app_folder_path}".format(bench_path=get_bench_path(),app_folder_path=supplier_rfq_app_folder_path)
		make_records(import_folder_path,fname)

def make_records(path, fname):
	if os.path.isdir(path):
		import_file_by_path("{path}/{fname}".format(path=path, fname=fname))


def create_custom_fields(**args):
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

    custom_fields = {
'Request for Quotation':[
 dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Request for Quotation',
  fetch_if_empty= 0,
  fieldname= 'project_cf',
  fieldtype= 'Link',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'vendor',
  label= 'Project',
  length= 0,
  name= 'Request for Quotation-project_cf',
  no_copy= 0,
  options= 'Project',
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
  'Request for Quotation':[
 dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Request for Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_comparison_section',
  fieldtype= 'Section Break',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'items',
  label= 'Supplier Comparison',
  length= 0,
  name= 'Request for Quotation-supplier_comparison_section', 
  no_copy= 0,
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
 'Request for Quotation':[
dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 1,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Request for Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_quotation_comparisons',
  fieldtype= 'Table',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'supplier_comparison_section',
  label= '',
  length= 0,
  name= 'Request for Quotation-supplier_quotation_comparisons',
  no_copy= 0,
  options= 'Supplier Quotation Comparison CT',
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
'Supplier Quotation Item':[
 dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Supplier Quotation Item',
  fetch_if_empty= 0,
  fieldname= 'schedule_date',
  fieldtype= 'Date',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 1,
  in_standard_filter= 0,
  insert_after= 'item_name',
  label= 'Required Date',
  length= 0,
  name= 'Supplier Quotation Item-schedule_date',
  no_copy= 0,
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
'Supplier Quotation':[
 dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Supplier Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_uploaded_attachment_cf',
  fieldtype= 'Attach',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'supplier_name',
  label= 'Supplier Uploaded Attachment',
  length= 0,
  name= 'Supplier Quotation-supplier_uploaded_attachment_cf',
  no_copy= 0,
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0,
 )
 ],
'Supplier Quotation':[
 dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Supplier Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_comparison',
  fieldtype= 'Section Break',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'amended_from',
  label= 'Supplier Comparison',
  length= 0,
  name= 'Supplier Quotation-supplier_comparison',
  no_copy= 0,
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
 'Supplier Quotation':[
dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 1,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Supplier Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_quotation_comparisons',
  fieldtype= 'Table',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'supplier_comparison',
  label= '',
  length= 0,
  name= 'Supplier Quotation-supplier_quotation_comparisons',
  no_copy= 0,
  options= 'Supplier Quotation Comparison CT',
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 1,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ],
 'Supplier Quotation':[
dict(
  allow_in_quick_entry= 0,
  allow_on_submit= 0,
  bold= 0,
  collapsible= 0,
  columns= 0,
  docstatus= 0,
  doctype= 'Custom Field',
  dt= 'Supplier Quotation',
  fetch_if_empty= 0,
  fieldname= 'supplier_notes',
  fieldtype= 'Text',
  hidden= 0,
  ignore_user_permissions= 0,
  ignore_xss_filter= 0,
  in_global_search= 0,
  in_list_view= 0,
  in_standard_filter= 0,
  insert_after= 'terms',
  label= 'Supplier Notes',
  length= 0,
  name= 'Supplier Quotation-supplier_notes',
  no_copy= 0,
  permlevel= 0,
  print_hide= 0,
  print_hide_if_no_value= 0,
  read_only= 0,
  report_hide= 0,
  reqd= 0,
  search_index= 0,
  translatable= 0,
  unique= 0
 )
 ]
 }

    create_custom_fields(custom_fields)
    frappe.db.commit()  # to avoid implicit-commit errors				

	