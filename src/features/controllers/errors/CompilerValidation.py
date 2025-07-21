from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

class CodeForm(FlaskForm):
    def validateCode(self, field):
        """
        Validador para el c digo a compilar.
        
        Verifica si el c digo est  vac o o tiene espacios en blanco.
        
        Parameters
        ----------
        field : str
            El campo que se va a validar.
        
        Raises
        ------
        ValidationError
            Si el c digo est  vac o o tiene espacios en blanco.
        """
        if not field.data or field.data.strip() == '':
            raise ValidationError('Code is with space, this input is required.')

    def validateLang(self, field):
        """
        Validador para el lenguaje de programaci n que se va a utilizar.
        
        Verifica si el lenguaje es permitido en este compilador y si el campo
        est  vac o tiene espacios en blanco.
        
        Parameters
        ----------
        field : str
            El campo que se va a validar.
        
        Raises
        ------
        ValidationError
            Si el lenguaje no es permitido o el campo est  vac o o tiene
            espacios en blanco.
        """
        if not field.data or field.data.strip() == '':
            raise ValidationError('Lang is with space, this input is required.')
        langPermited = ['python', 'c++', 'c#', 'java']
        # , 'rust', 'javascript', 'php', 'bash', 'go', 'kotlin', 'typescript', 'swift'
        if field.data not in langPermited:
            raise ValidationError('Language not permited in this compilator.')

    code = StringField('code', validators=[validateCode])
    lang = StringField('lang', validators=[validateLang])