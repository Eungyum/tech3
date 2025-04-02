from uuid import uuid4

def proof_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    filename = f"{uuid4().hex[:8]}_{filename}"
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/매출증빙/{key}_{filename}'

def process_upgrade_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    filename = f"{uuid4().hex[:8]}_{filename}"
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/공정개선율/{key}_{filename}'

def form1_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/기술실시결과보고서{ext}'

def form2_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/최종기술기여도{ext}'

def form3_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/매출액기여율산출의견서{ext}'

def form4_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/기술실시계약보고서{ext}'

def form5_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/기술료징수결과보고서{ext}'

def form6_file_dir(instance, filename):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    ext = os.path.splitext(filename)[1]
    return f'uploads/kimst/{unique_key}_{year}_{session}_직접실시/연구개발성과미실시확인서{ext}'

def folder_link(instance):
    user = instance.uniqueobject
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    return f'uploads/kimst/{unique_key}_{year}_{session}/'

def ntis_capture_file_dir(instance, filename):
    user = instance.uniqueobject  # ✅ 올바른 유저 접근
    unique_key = user.project.unique_key if user and hasattr(user, 'project') else 'anonymous'
    year = instance.year or 'unknown-year'
    session = instance.session or 'unknown-session'
    key = instance.id or 'unknown-key'
    filename = f"{uuid4().hex[:8]}_{filename}"
    return f'uploads/kimst/{unique_key}_{year}_{session}_미실시/ntis캡처파일/{key}_{filename}'
