from django import forms

CHOICES = (('1', 'First',), ('2', 'Second',))
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)



class ParentForm(forms.Form):
    #to take the input of username
    tdlistParent = forms.CharField(label='Please Enter To-do Area',max_length=50, widget=forms.TextInput(attrs={'class' : 'input'}))
    # to take the input of email
#    email = forms.CharField(max_length=100)
    # to take the input of password
#    password = forms.CharField(max_length=100)


class UnknownForm(forms.Form):
    date2 = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class ChildForm(forms.Form):
    tdlistChild = forms.CharField(label='Please Enter To-do activity', max_length=50, widget=forms.TextInput(attrs={'class':'input'}))


class CheckForm(forms.Form):
    choices = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
    )

'''


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match."))
        return password2

'''
