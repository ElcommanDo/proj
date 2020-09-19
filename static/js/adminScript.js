$(document).ready(function() {
  $('[data-toggle="tooltip"]').tooltip();
});

$('#seeAnotherField').change(function() {
  if ($(this).val() == 'yes') {
    $('#otherFieldDiv').show();
    $('#otherFieldDiv2').hide();
    $('#otherField').attr('required', '');
    $('#otherField').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldDiv').hide();
    $('#otherFieldDiv2').show();
    $('#otherField').removeAttr('required');
    $('#otherField').removeAttr('data-error');
  }
});
$('#seeAnotherField').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'القاهرة') {
    $('#otherFieldGroupDiv').show();
    $('#otherField1').attr('required', '');
    $('#otherField1').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv').hide();
    $('#otherField1').removeAttr('required');
    $('#otherField1').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'الجيزة') {
    $('#otherFieldGroupDiv2').show();
    $('#otherField2').attr('required', '');
    $('#otherField2').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv2').hide();
    $('#otherField2').removeAttr('required');
    $('#otherField2').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'البحيرة') {
    $('#otherFieldGroupDiv3').show();
    $('#otherField3').attr('required', '');
    $('#otherField3').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv3').hide();
    $('#otherField3').removeAttr('required');
    $('#otherField3').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'الاسكندرية') {
    $('#otherFieldGroupDiv4').show();
    $('#otherField4').attr('required', '');
    $('#otherField4').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv4').hide();
    $('#otherField4').removeAttr('required');
    $('#otherField4').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'سوهاج') {
    $('#otherFieldGroupDiv5').show();
    $('#otherField5').attr('required', '');
    $('#otherField5').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv5').hide();
    $('#otherField5').removeAttr('required');
    $('#otherField5').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'قنا') {
    $('#otherFieldGroupDiv6').show();
    $('#otherField6').attr('required', '');
    $('#otherField6').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv6').hide();
    $('#otherField6').removeAttr('required');
    $('#otherField6').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'اسيوط') {
    $('#otherFieldGroupDiv7').show();
    $('#otherField7').attr('required', '');
    $('#otherField7').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv7').hide();
    $('#otherField7').removeAttr('required');
    $('#otherField7').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'المنيا') {
    $('#otherFieldGroupDiv8').show();
    $('#otherField8').attr('required', '');
    $('#otherField8').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv8').hide();
    $('#otherField8').removeAttr('required');
    $('#otherField8').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');

$('#seeAnotherFieldGroup').change(function() {
  if ($(this).val() == 'بني سويف') {
    $('#otherFieldGroupDiv9').show();
    $('#otherField9').attr('required', '');
    $('#otherField9').attr('data-error', 'This field is required.');
  } else {
    $('#otherFieldGroupDiv9').hide();
    $('#otherField9').removeAttr('required');
    $('#otherField9').removeAttr('data-error');
  }
});
$('#seeAnotherFieldGroup').trigger('change');




















