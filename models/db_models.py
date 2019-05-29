db.define_table(
    'tipo_contas'
    ,Field('tipo',notnull=True)
    ,format="%(tipo)s"
)

db.define_table(
	'contas'
	,Field('tipo','reference tipo_contas', notnull=True)
    ,Field('descricao',notnull=True)
    ,Field('conta_pai','reference contas')
	,format="%(descricao)s"
)
