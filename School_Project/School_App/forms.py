from django import forms
from . models import Student, Course

GENDER_CHOICES = [('Male','Male'),('Female','Female')]
MATERIAL_CHOICE = [
    ('Note Books','Note books'),
    ('Academic Books','Academic Books'),
    ('Stationery Supplies','Stationery Supplies'),
    ('Uniform','Uniform'),
    ('Lab Utilities','Lab Utilities')

]
class StudentForm(forms.ModelForm):
    gender = forms.ChoiceField(choices= GENDER_CHOICES,widget=forms.RadioSelect)
    materials_provided = forms.MultipleChoiceField(label='Materials Provided', choices=MATERIAL_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Student
        fields = ('name','dob','age','gender','phone','mail','address','department','course','purpose','materials_provided')
        labels = {'name':'Name','dob':'Date Of Birth','age':'Age','gender':'Gender','phone':'Phone Number','mail':'Email ID','address':'Address','department':'Department','course':'Course','purpose':'Purpose','materials_provided':'Materials Provided'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mail':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-select'}),
            'course':forms.Select(attrs={'class':'form-select'}),
            'purpose':forms.Select(attrs={'class':'form-control'}),
            
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')

            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
            