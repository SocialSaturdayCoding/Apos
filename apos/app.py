from apos.extensions import db, app, api
from apos.resources.coupons import CouponResource, CouponListResource
from apos.resources.auth import Auth, Signup

api.add_resource(CouponResource, '/api/v1/coupons/<int:coupon_id>')
api.add_resource(CouponListResource, '/api/v1/coupons')
api.add_resource(Auth, '/api/v1/auth')
api.add_resource(Signup, '/api/v1/signup')

if __name__ == '__main__':
    app.run()
