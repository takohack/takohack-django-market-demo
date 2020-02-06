from django.shortcuts import render,redirect
from market.models import Goods
from PIL import Image

from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator


# Create your views here.

def index(request):

    goods = Goods.objects.all()

    p = Paginator(goods,3)
    p1 = p.count
    p2 = p.num_pages
    p3 = p.page_range
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        book_list = p.page(current_num)
    except:
        book_list = p.page(1)
    pageRange = p.page_range

    if not request.session.get('is_login', None):
        return render(request,'market/index_not_login.html',locals())
    return render(request,'market/index.html',locals())




def add(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        username = request.session.get('user_name',None)
        phone = request.POST['phone']
        title = request.POST['title']
        price = request.POST['price']
        if price=='':
            message = "请填写价格"
            return render(request, 'market/add.html', locals())
        # noinspection PyBroadException
        try:
            img = request.FILES['img']
        except:
            message = "请上传图片"
            return  render(request,'market/add.html',locals())
        image = Image.open(img)
        width, height = image.size
        rate =1.0
        if width >= 2000 or height >= 2000:
            rate = 0.3
        elif width >= 1000 or height >= 1000:
            rate = 0.5
        elif width >= 500 or height >= 500:
            rate = 0.9
        width = int(width * rate)
        height = int(height * rate)

        image.thumbnail((width, height), Image.ANTIALIAS)
        pic_io = BytesIO()
        image.save(pic_io, image.format)
        pic_file = InMemoryUploadedFile(
            file=pic_io,
            field_name=None,
            name=img.name,
            content_type=img.content_type,
            size=img.size,
            charset=None
        )

        cate = request.POST['cate']
        describe = request.POST['describe']
        new_goods = Goods(username=username,phone=phone,title=title, price=price, img=pic_file, cate=cate,describe=describe)
        new_goods.save()
        return redirect('/')
    message = "上传图片有点慢,图片上传成功会自动跳转"
    return render(request, 'market/add.html',locals())

def personal(request):
    username = request.session.get('user_name', None)
    goods = Goods.objects.filter(username=username)

    context = {
        'goods': goods
    }
    if not request.session.get('is_login', None):
        return render(request, 'market/index_not_login.html', context)
    return render(request, 'market/personal.html', context)

def need(request):
    return render(request,'market/need.html')

def detail(request,id):
    goods = Goods.objects.filter(id=id)

    context = {
        'goods': goods
    }
    if not request.session.get('is_login', None):
        return render(request, 'market/detail_not_login.html', context)
    return render(request, 'market/detail.html', context)
def delete(request,id):
    if not request.session.get('is_login', None):
        return render(request, 'market/index_not_login.html')
    goods = Goods.objects.filter(id=id)
    username = request.session.get('user_name', None)
    if username==goods[0].username:
        goods.delete()
        return redirect("/personal")

def other(request):
    goods = Goods.objects.filter(cate="其他")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)
def book(request):
    goods = Goods.objects.filter(cate="图书")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)

def life(request):
    goods = Goods.objects.filter(cate="生活日用")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)
def cloths(request):
    goods = Goods.objects.filter(cate="服饰鞋子")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)
def service(request):
    goods = Goods.objects.filter(cate="技能服务")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)
def dianqi(request):
    goods = Goods.objects.filter(cate="家用电器")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)

def tech(request):
    goods = Goods.objects.filter(cate="电子数码")
    context = {
        'goods': goods
    }

    if not request.session.get('is_login', None):
        return render(request, 'market/categories_not_login.html', context)
    return render(request, 'market/categories.html', context)




