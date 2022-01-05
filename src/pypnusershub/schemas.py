from marshmallow import pre_load, fields

from utils_flask_sqla.schema import SmartRelationshipsMixin

from pypnusershub.env import MA, db
from pypnusershub.db.models import User, Organisme


class UserSchema(SmartRelationshipsMixin, MA.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        load_instance = True
        sqla_session = db.session
        exclude = (
            "_password",
            "_password_plus",
        )

    nom_complet = fields.String()
    groups = fields.Nested('self', many=True)

    # TODO: remove this and fix usage of the schema
    @pre_load
    def make_observer(self, data, **kwargs):
        if isinstance(data, int):
            return dict({"id_role": data})
        return data


class OrganismeSchema(SmartRelationshipsMixin, MA.SQLAlchemyAutoSchema):
    class Meta:
        model = Organisme
        load_instance = True
        sqla_session = db.session
