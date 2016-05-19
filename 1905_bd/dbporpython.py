#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
database = sqlite3.connect('pos_empresa.db')
cursor = database.cursor()

print
"""¿Cantidad total de ventas en el año 2013? (sale → gross_total)"""
cursor.execute("select count(gross_total) FROM sale where date LIKE '2013%'")
for i in cursor:
	print "Cantidad de ventas año 2013 = ",i[0]
print

"""¿Precio promedio de venta por producto? (sale_product → net_unit_price)"""
cursor.execute("SELECT product.name,AVG(sale_product.net_unit_price) AS \"Precio promedio de venta por producto\" FROM sale_product JOIN product ON product.id = sale_product.product_id GROUP BY product.id LIMIT 10")
for i in cursor:
	print "Producto: " ,i[0]," | ", "Precio promedio de venta: ",i[1]
print

"""¿Total de ventas (gross_total) por cliente? (sale→ gross_total)"""
cursor.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id GROUP BY entity_id LIMIT 10")
for i in cursor:
	print "Nombre: ",i[0] ," | ","Apellido: ",i[1]," | ","Compañia: ",i[2]," | ","Total de ventas: ",i[3]
print

"""¿Total de ventas por cliente en el año 2014? (sale → gross_total)"""
cursor.execute("SELECT entity.names,entity.surnames,entity.company_name,SUM(gross_total) FROM sale JOIN entity ON entity.id = sale.entity_id WHERE sale.date LIKE '2014%' GROUP BY entity_id LIMIT 10")
for i in cursor:
	print "Nombre: ",i[0] ," | ","Apellido: ",i[1]," | ","Compañia: ",i[2]," | ","Total de ventas: ",i[3]
print

"""¿Cantidad y monto total de ventas por día en noviembre de 2013?"""
cursor.execute("SELECT date, COUNT(*), SUM(gross_total) FROM sale WHERE date LIKE '2013-11%' GROUP BY date LIMIT 10")
for i in cursor:
	print "Fecha: ",i[0] ," | ","Cantidad de ventas: ",i[1]," | ","Total de ventas: ",i[2]
print

"""¿Cantidad y montos totales agrupados por producto en orden 
descendente según cantidad? (sale_product → quantity, gross_total)"""
cursor.execute("SELECT product.name, sale_product.quantity, sale_product.gross_total FROM sale_product JOIN product ON sale_product.product_id = product.id ORDER BY sale_product.quantity DESC LIMIT 10")
for i in cursor:
	print "Producto: ",i[0] ," | ","Cantidad: ",i[1]," | ","Total de ventas: ",i[2]
print


database.commit()
cursor.close()
database.close()


