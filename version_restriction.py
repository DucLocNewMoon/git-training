from firebase_admin import credentials, firestore, initialize_app


firebase_credentials = {
    "type": "service_account",
    "project_id": "any-browser-b17b5",
    "private_key_id": "13157bd8832d99ac739cf916f32eeeed7fe9d7a8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4KGW3laBacwry\nWGXKDFHkv+yXu4exJEccPam8/m2gTgPaSLH5j6M1F0XnoTIsWRHuo+zO6Owbus4o\nH+8szajezbIAtI9QBxUtKJtWhRyMJD+eSLE37toXPJYsKTFpjKxJPkySwNW8F5HW\nJgGszz3B5A527n09XLAK5HYTpqGY4wI3V3HTxzfob3nnKMxUV803s6XxxGe+9KwF\nRYKMrHqdQDhOyhl0dwBDxy5We/eNgxgfSmvinUxq9UMqRTNf/oGKzqE8xjcbI1rJ\n8br/TdwpyGjd969D3v8S/4drydqSWRrES99j9fIwnlDLue7ORAOREcCHFg2onkCT\n60iVtPfPAgMBAAECggEAMY9FmHte9RiCuKeLdS2NmHcCD+962/Q8YuBBXshF7l8w\ncD0iEFxUesQxnt1lqEOsLMHWx/QtHmVOd8PoVPFf4d4PalstOkc9rrJ/42/dN+XF\nbS546umPrbMzYt0PHC2sa+WlK9VTb9QT/kKqLrxzDUv3jJAwCiR4h+Xl1PICCSeQ\nhatfRNk/YAm73NZXVi9ZHxxjt5sMlbPDboUrcqFLRMBwFgYZ9F5AEtCiWqlKpaFj\nrv7FAkv16DGiYiu+Vs+3WH/FJJu+BmXVHY2KrvOewvPFfYsmqTu8d/W0l7h4qBSA\nznWmk1cj0txCm42qt+AmNvJDKC48QA8Mlcf4GUY76QKBgQD5NzIVDagWX8UhpZbb\n8m6nDweTuYYC1EJvf1LdQTXuVkT3MjnNvBJf3w+qPvfpCVB0vgIPjHtivBumVrmS\nGpoiS9t25ralzS+hpAnj4N8GwdDC8kdssCE45c3282nwLZisls2JX0eNkNwsXvqb\nKA1SquM0vEVk3rrZVP0+guQnJQKBgQC9K870staYufThYo9ATwCZyvEXmtUkw6zO\nTqMeaQxbrjsBndS76fkfWsr6YmOYyW78nL5pH4cX8JwAuJMn45qn2LR3Taw/R05n\ntrJ3J0hb0hfHHJvr8kV20DGg/x2trx+4/P4RJSBRhbtbZUSoNJe1ItjrwjO3sPKB\nBt13DFKa4wKBgEZt49hxUJRqIlLc8iJchArwQ2rrHkVEaTYLXIasvCoL9VeKuS08\nPlEbv9iUDQmtmTA01m5AfEot8P50OeNhYzfYCkCy+OEoeJKMwkLFNSI6ud2uDKNZ\nrzneL/PfXIwExsXXpGRzKcyHKMHdYaNhkUpQgv9PSak1DMcIrrzwzruFAoGAUHOx\nMKBeY9WyL6ibA96VgtKsdj2DKH+Pnq4S8Xv7pYIT1jwpnUGEkbErYhE2CmSgrw56\nbHrcGXJa5nOZIf3KaFfhaFvARaktzy4D+GjcfTB8rFGefloq8LzaXn4hQRyZgTMX\nWnNPq1wUsmn/KQo0+vQ3DQ0qsZSvjfA9f8Pd3cECgYEA68ALQQSqJyvGAmsL2yMk\nBgIaKD3Ced2Vl9FRC2uuLs1zu1OxLPd30Oo+XqqG1wQO4PHsH8Xuhn46bRfqBH5E\nRVLruleShbWYUUXi1FmiBo/WwsZcuj3YOJXsCbXvy8bUemp7A9zCKmhMunCWMYJj\nzSbf2UCTl1hXSFdPCRLtOyc=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-sifr3@any-browser-b17b5.iam.gserviceaccount.com",
    "client_id": "115820401961838552295",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-sifr3%40any-browser-b17b5.iam.gserviceaccount.com"
}


def _get_firestore_db():
    cred = credentials.Certificate(firebase_credentials)
    initialize_app(cred)
    return firestore.client()


def check_version_restriction(app_version):
    db = _get_firestore_db()
    document = db.collection('version_read_hotmail_gmail').document(app_version).get()
    
    if document.exists:
        is_active = document.to_dict().get('is_active')
        return is_active
    else:
        return None