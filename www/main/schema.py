import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

# model fields
from orders.models import Order, OrderItem
from shop.models import Product,ProductVarietie,ProductUnit,Price,ProductCategorie,ProductSubCategorie,ProductGrade,ProductImage


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id","delivery_address","delivery_instructions","order_status","fulfilment_status","payment_status","timestamp","datestamp")
    

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = ("id","order","product_grade","quantity","product")


class ProductSubCategoryType(DjangoObjectType):
    class Meta:
        model = ProductSubCategorie
        fields = ("id","category","name")

class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategorie
        fields = ("id","name")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id","name","subcategory")
        
class ProductVarietyType(DjangoObjectType):
    class Meta:
        model = ProductVarietie
        fields = ("id","product","name")

class ProductUnitType(DjangoObjectType):
    class Meta:
        model = ProductUnit
        fields = ("id","product","unit","unit_abbr")

class ProductPriceType(DjangoObjectType):
    class Meta:
        model = Price
        fields = ('id','value','currency')

class ProductGradeType(DjangoObjectType):
    class Meta:
        model = ProductGrade
        fields = ('id','product','unit','grade','description','price')



class OrderMutation(graphene.Mutation):
    class Arguments:
        quantity = graphene.String()
        id = graphene.ID()
    order = graphene.Field(OrderItemType)

    @classmethod
    def mutate(cls,root,info,quantity,id):
        order = OrderItem.objects.get(pk=id)
        order.quantity = quantity
        order.save(update_fields=['quantity'])
        return OrderMutation(order=order)

class Mutations(graphene.ObjectType):
    update_order = OrderMutation.Field()


class Query(graphene.ObjectType):
    all_product_grades = graphene.List(ProductGradeType, search=graphene.String(), category=graphene.String())
    order_product_by_id = graphene.Field(OrderItemType,product=graphene.String(required=True),order=graphene.String(required=True))

    def resolve_order_product_by_id(root,info,product,order,**kwargs):
        try:
           qs = OrderItem.objects.get(product_grade_id=product,order_id=order)
        except OrderItem.DoesNotExist:
            qs = None
        return qs
    
    def resolve_all_product_grades(root,info,search=None,category=None,**kwargs):
        if search:
            if category:
                filter = (
                    Q(grade__exact='A') & (
                        (
                            Q(product__product__subcategory__name__exact= category)|
                            Q(product__product__subcategory__category__name__icontains=category)
                        ) &
                        (
                            Q(product__product__name__icontains = search) |
                            Q(product__name__icontains = search)
                        )
                    )
                )
            else:
                filter = (
                    Q(grade__exact='A') & (
                        Q(product__product__name__icontains = search) |
                        Q(product__name__icontains = search)
                    )
                )
            return ProductGrade.objects.filter(filter)
        elif category:
            filter = (
                    Q(grade__exact='A') & (
                    Q(product__product__subcategory__name__exact= category)|
                    Q(product__product__subcategory__category__name__icontains=category)
                    )
            )
            return ProductGrade.objects.filter(filter)
        return ProductGrade.objects.filter(grade__exact='A')
    
schema = graphene.Schema(query=Query,mutation=Mutations)