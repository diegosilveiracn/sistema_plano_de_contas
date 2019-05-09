db.define_table(
	'contas_tipo'
	,Field('tipo', notnull=True)
	,format="%(tipo)s"
)
db.define_table(
	'contas_categoria'
	,Field('tipo','reference contas_tipo',  notnull=True)
	,Field('categoria', notnull=True)
	,format="%(categoria)s"
)

db.define_table(
	'contas_itens'
	,Field('item')
	,Field('categoria','reference contas_categoria')
	,format="%(item)s"
)

db.define_table(
	'contas'
	,Field('valor','double',default=0)
	,Field('item','reference contas_itens')
	)

