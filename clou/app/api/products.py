from flask_restx import Namespace, Resource, fields, marshal
from app.services.facade import facade
from werkzeug.exceptions import BadRequest


api = Namespace('product', description='product operations')
error = BadRequest('Invalid input data')

# Define the Product  model for input validation and documentation
product_model = api.model('Product_input', {
    'description': fields.String(required=True, description='description of the product'),
    'price': fields.Float(required=True, description='price of the product'),
    'qty': fields.Integer(required=True, description='quantity of product availlable')
    })

product_response_model = api.model('Product_response', {
    'id':fields.String(required=True, descritpion='id of the product'),
    'description': fields.String(required=True, description='description of the product'),
    'price': fields.Float(required=True, description='price of the product'),
    'qty': fields.Integer(required=True, description='quantity of product availlable')
    })

@api.route('/')
class ProductCreate(Resource):
    @api.expect(product_model, validate=True)
    @api.response(201, 'product successfully created')
    @api.response(400, 'Invalid input data')

    def post(self):
        """Register a new Product"""
        product_data = api.payload
        try:
            new_product = facade.create_product(product_data)
        except (TypeError, ValueError):
            raise error
        return marshal(new_product, product_response_model), 201
    
    def get(self):
        """Returns a list of product"""
        return {"message": "List of product"}
"""
@api.route('/product_id>')
class ProductResource(Resource):
    @api.response(200, 'product details retrieved successfully')
    @api.response(404, 'product not found')
    @api.marshal_with(product_model, code=201)
    def get(self, product_id):
        #Get user details by ID
        user = facade.get_user(user_id)
        if not user:
            raise error 
        else:
            return marshal(product, product_model), 201
    
    @api.expect(product_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.marshal_with(product_model, code=201)
    def put(self, user_id):
        #Update product details
        pass
"""
