import sqlparse
#query='select * from someschema where a>7;'
#query='select col1, col2 from table_name;'
def pquery(query):
	parsedQuery = sqlparse.parse(query[:-1])[0].tokens
	identifierList = []
	l = sqlparse.sql.IdentifierList(parsedQuery).get_identifiers()
	for i in l:
		identifierList.append(str(i))
	return identifierList