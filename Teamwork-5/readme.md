# Personnel

'''
Deparment ve Personnel tablolarımız olacak bunları birbirlerine bağlayacağız. .her deparmentın altında kendisine ait personel olacak.
Staff olan personel yeni personel listeye ekleyebilecek, update edebilecek.(staff dan kasıt yetkili olan bunu farklı cheff de diyebilirsiniz.Staff ismi django user modelinde bulunan is_staff dan geliyor )
Dinamik url ile url de gelen isteğe göre response değişecek.Yani departmenlara ait personeli listelemek istediğimizde bunu tek bir url üzerinden yapacağız.Swagger da örneği var.
Staff olmayanlar sadece listeleyebilecek
Personeli silme yetkisi sadece superuserlarda olacak.
Token authentication kullanacağız. Kullanıcı logout olduğunda tokeni sileceğiz.

user - list, get 
staff - create, update, patch
superuser - delete
'''