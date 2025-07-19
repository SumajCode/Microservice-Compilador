from features.controllers.errors.CompilerValidation import CodeForm
from wtforms import StringField
from wtforms.validators import ValidationError

class AssetForm(CodeForm):
    def validateInputs(self, field):
        """
        Validates the inputs input.

        The inputs input is required for testing a function. This method
        checks if the input is empty or has a length of zero. If either
        condition is true, a ValidationError is raised with an appropriate
        error message.

        Parameters
        ----------
        field : str
            The inputs input to validate.

        Raises
        ------
        ValidationError
            If the input is empty or has a length of zero.
        """
        if not field.data:
            raise ValidationError('Inputs is required for testing function.')
        if len(field.data) == 0:
            raise ValidationError('Inputs length must be greater than 0.')

    def validateOutputs(self, field):
        """
        Validates the outputs input.

        The outputs input is required for testing a function. This method
        checks if the input is empty or has a length of zero. If either
        condition is true, a ValidationError is raised with an appropriate
        error message.

        Parameters
        ----------
        field : str
            The outputs input to validate.

        Raises
        ------
        ValidationError
            If the outputs input is empty or has a length of zero.
        """

        if not field.data:
            raise ValidationError('Outputs is required for testing function.')
        if len(field.data) == 0:
            raise ValidationError('Outputs length must be greater than 0.')

    def validateFunctionInvoke(self, field):
        """
        Validates the function invoke input.

        The function invoke input is required to test a function. This method
        checks if the input is empty or contains only whitespace characters.
        If either condition is true, a ValidationError is raised with an
        appropriate error message.

        Parameters
        ----------
        field : str
            The function invoke input to validate.

        Raises
        ------
        ValidationError
            If the function invoke input is empty or contains only whitespace
            characters.
        """
        if not field.data or field.data.strip() == '':
            raise ValidationError('Function invoke is required for testing function.')

    inputs = StringField('inputs', validators=[validateInputs])
    outputs = StringField('outputs', validators=[validateOutputs])
    functionInvoke = StringField('outputs', validators=[validateFunctionInvoke])