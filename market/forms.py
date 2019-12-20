from django import forms

class AddForm(forms.Form):
    categories = (
        ('tech', "电子数码"),
        ('dianqi', "家用电器"),
        ('service', "技能服务"),
        ('cloths', "服饰鞋子"),
        ('life', "生活日用"),
        ('book', "图书"),
        ('other', "其他"),
    )
    phone = forms.CharField(label="QQ", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="商品名称", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label="价格")
    img = forms.ImageField(label="图片")
    cate = forms.ChoiceField(label="分类", choices=categories)
    describe =forms.CharField(label="商品描述",max_length=300,widget=forms.Textarea(attrs={'class': 'form-control'}))
