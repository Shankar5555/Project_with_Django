from dairy import forms
from dairy.forms import LoginForm
from django.contrib import auth
from django.urls import path
from dairy import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordConfirmForm, MyPasswordResetForm,feedbackForm
from django.contrib import admin

urlpatterns = [
   
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('customer', views.customer),
    path('orderplaced', views.orderplaced),
    path('carts', views.carts),
    path('product', views.product),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password__reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MyPasswordConfirmForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('freshmilk/', views.freshmilk, name='freshmilk'),
    path('freshmilk/<slug:data>', views.freshmilk, name='freshmilkdata'),
    path('paneer/', views.paneer, name='paneer'),
    path('paneer/<slug:data>', views.paneer, name='paneerdata'),
    path('chaas/', views.chaas, name='chaas'),
    path('chaas/<slug:data>', views.chaas, name='chaasdata'),
path('lassi/', views.lassi, name='lassi'),
    path('lassi/<slug:data>', views.lassi, name='lassidata'),
path('flavourmilk/', views.flavourmilk, name='flavourmilk'),
    path('flavourmilk/<slug:data>', views.flavourmilk, name='flavourmilkdata'),
path('ghee/', views.ghee, name="ghee"),
    path('ghee/<slug:data>', views.ghee, name='gheedata'),
path('butter/', views.butter, name='butter'),
    path('butter/<slug:data>', views.butter, name='butterdata'),
path('cream/', views.cream, name='cream'),
    path('cream/<slug:data>', views.cream, name='creamdata'),
path('cheese/', views.cheese, name='cheese'),
    path('cheese/<slug:data>', views.cheese, name='cheesedata'),
path('dahi/', views.dahi, name='dahi'),
    path('dahi/<slug:data>', views.dahi, name='dahidata'),
path('shrikhand/', views.shrikhand, name='shrikhand'),
    path('shrikhand/<slug:data>', views.shrikhand, name='shrikhanddata'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerregistration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('feedbacks/',views.Feedbacks.as_view(), name='feedbacks'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
