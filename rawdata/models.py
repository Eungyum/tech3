from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from decimal import Decimal, ROUND_HALF_UP
from PIL import Image
from .utils import gen_unique_code

# 전담기관
class Agency(models.Model):
    fullname = models.CharField(max_length=30, verbose_name="전담기관 이름", null=True, blank=True) # 국토교통과학기술진흥원
    name = models.CharField(max_length=15, verbose_name="전담기관 약어", null=True, blank=True) # kaia
    logo = models.ImageField(verbose_name="로고 이미지", null=True, blank=True, upload_to='agency/logos/') # 대표 로고 이미지
    logosmall = models.ImageField(verbose_name="작은로고", null=True, blank=True, upload_to='agency/logos/') # 줄어들었을때 로고 이미지
    class Meta: # 테이블명 : 전담기관
        verbose_name = "전담기관"
        verbose_name_plural = "전담기관"
    def __str__(self): # 대표명칭은 kimst, keiti 등
        return f"{self.name}"
    def save(self, *args, **kwargs): # logo 이미지 저장방식
        super().save(*args, **kwargs)
        if self.logo:
            try:
                img = Image.open(self.logo.path)
                if img.width != 20:
                    w_percent = 20 / float(img.width)
                    h_size = int(float(img.height) * w_percent)
                    img = img.resize((20, h_size), Image.ANTIALIAS)
                    img.save(self.logo.path)
            except Exception as e:
                pass

# 프로젝트
class Project(models.Model):
    agency_info = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name='전담기관정보', null=True, blank=True) # 전담기관
    project_id = models.CharField(max_length=5, unique=True, blank=True) # 불특정아이디
    businessname1 = models.CharField(max_length=255, verbose_name="사업명", null=True, blank=True)
    businessname2 = models.CharField(max_length=255, verbose_name="내역사업명", null=True, blank=True)
    ntis_code = models.CharField(max_length=20, verbose_name="NTIS번호", unique=True, null=True, blank=True)
    iris_code = models.CharField(max_length=20, verbose_name="아이리스코드", null=True, blank=True)
    etc_code = models.CharField(max_length=20, verbose_name="과제번호2", null=True, blank=True)
    title1 = models.CharField(max_length=255, verbose_name="최상위과제명", null=True, blank=True)
    title2 = models.CharField(max_length=255, verbose_name="세부과제명", null=True, blank=True)
    maincompany = models.CharField(max_length=100, verbose_name="주관연구기관", null=True, blank=True)
    mainresearcher = models.CharField(max_length=100, verbose_name="주관연구책임자", null=True, blank=True)
    costgov = models.IntegerField(verbose_name="총연구개발비(정부)", null=True, blank=True)
    costcompany = models.IntegerField(verbose_name="총연구개발비(기업)", null=True, blank=True)
    costregion = models.IntegerField(verbose_name="총연구개발비(지방)", null=True, blank=True)
    costetc = models.IntegerField(verbose_name="총연구개발비(기타)", null=True, blank=True)
    cost = models.IntegerField(verbose_name="총연구개발비(합계)", null=True, blank=True)
    dateengage = models.DateField(verbose_name="연구협약일", null=True, blank=True)
    datestart = models.DateField(verbose_name="연구개발시작일", null=True, blank=True)
    dateend = models.DateField(verbose_name="연구개발종료일", null=True, blank=True)
    datesettle = models.DateField(verbose_name="정산일", null=True, blank=True)
    companies = models.ManyToManyField('Company', verbose_name='공동연구개발기관', blank=True)
    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = gen_unique_code(Project, 'project_id', length=5)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "과제"
        verbose_name_plural = "과제"
    def __str__(self):
        return f"{self.agency_info}_{self.title2}"
    
# 실시기관
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="기업명", null=True, blank=True)
    company_id = models.CharField(max_length=5, unique=True, blank=True)
    companycode = models.CharField(max_length=12, verbose_name="사업자번호", unique=True, null=True, blank=True)
    ceo = models.CharField(max_length=50, verbose_name="대표자", null=True, blank=True)
    type = models.CharField(max_length=50, verbose_name="기업타입", null=True, blank=True)
    rate_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="기업요율")
    field = models.CharField(max_length=50, verbose_name="업종", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="주소", null=True, blank=True)
    tel = models.CharField(max_length=15, verbose_name="전화번호", null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name="이메일", null=True, blank=True)
    homepage = models.CharField(max_length=255, verbose_name='홈페이지', null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.company_id:
            self.company_id = gen_unique_code(Company, 'company_id', length=5)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "실시기관"
        verbose_name_plural = "실시기관"
    def __str__(self):
        return f"{self.name}"
    
# 프로젝트 x 실시기관
class UniqueObject(models.Model):
    name = models.CharField(max_length=50, verbose_name="고유정보명칭",  null=True, blank=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='기업정보', to_field='company_id', null=True, blank=True)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='과제정보', to_field='project_id', null=True, blank=True)
    unique_key = models.CharField(max_length=20, verbose_name="키", null=True, blank=True, unique=True)
    title3 = models.CharField(max_length=255, verbose_name="기술실시 대상과제명", null=True, blank=True)
    datestart = models.DateField(verbose_name="연구개발시작일(기업별)", null=True, blank=True)
    dateend = models.DateField(verbose_name="연구개발종료일(기업별)", null=True, blank=True)
    researcher = models.CharField(max_length=100, verbose_name="기업연구책임자", null=True, blank=True)
    tel = models.CharField(max_length=15, verbose_name="전화번호", null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name="이메일", null=True, blank=True)
    firstreportyear = models.IntegerField(verbose_name="최초보고년도", null=True, blank=True)
    costgov = models.IntegerField(verbose_name="기업연구개발비(정부)", null=True, blank=True)
    costcompany = models.IntegerField(verbose_name="기업연구개발비(기업)", null=True, blank=True)
    costregion = models.IntegerField(verbose_name="기업연구개발비(지방)", null=True, blank=True)
    costetc = models.IntegerField(verbose_name="기업연구개발비(기타)", null=True, blank=True)
    cost = models.IntegerField(verbose_name="기업연구개발비(합계)", null=True, blank=True)
    @property
    def rategov(self):
        if self.cost and self.costgov > 0 and self.cost is not None:
            rate = (Decimal(self.costgov) / Decimal(self.cost)) * Decimal(100)
            return rate.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return Decimal('0.00')
    sizerate = models.DecimalField(verbose_name="기업요율", max_digits=5, decimal_places=2, null=True, blank=True)
    status_1year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_2year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_3year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_4year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_5year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_6year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_7year = models.IntegerField(verbose_name="1년차 보고년도", null=True, blank=True)
    status_1year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_2year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_3year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_4year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_5year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_6year_switch = models.BooleanField(default=True, null=True, blank=True)
    status_7year_switch = models.BooleanField(default=True, null=True, blank=True)
    grant1 = models.IntegerField(verbose_name="정산지원금(1차년도)", null=True, blank=True)
    grant2 = models.IntegerField(verbose_name="정산지원금(2차년도)", null=True, blank=True)
    grant3 = models.IntegerField(verbose_name="정산지원금(3차년도)", null=True, blank=True)
    grant4 = models.IntegerField(verbose_name="정산지원금(4차년도)", null=True, blank=True)
    grant5 = models.IntegerField(verbose_name="정산지원금(5차년도)", null=True, blank=True)
    grant6 = models.IntegerField(verbose_name="정산지원금(6차년도)", null=True, blank=True)
    grant7 = models.IntegerField(verbose_name="정산지원금(7차년도)", null=True, blank=True)
    agreegrant = models.IntegerField(verbose_name="협약정부지원금(총)", null=True, blank=True)
    agreegrant1 = models.IntegerField(verbose_name="협약정부지원금(1차년도)", null=True, blank=True)
    agreegrant2 = models.IntegerField(verbose_name="협약정부지원금(2차년도)", null=True, blank=True)
    agreegrant3 = models.IntegerField(verbose_name="협약정부지원금(3차년도)", null=True, blank=True)
    agreegrant4 = models.IntegerField(verbose_name="협약정부지원금(4차년도)", null=True, blank=True)
    agreegrant5 = models.IntegerField(verbose_name="협약정부지원금(5차년도)", null=True, blank=True)
    agreegrant6 = models.IntegerField(verbose_name="협약정부지원금(6차년도)", null=True, blank=True)
    agreegrant7 = models.IntegerField(verbose_name="협약정부지원금(7차년도)", null=True, blank=True)
    agreerate1 = models.DecimalField(verbose_name="협약기술기여도(1차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate2 = models.DecimalField(verbose_name="협약기술기여도(2차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate3 = models.DecimalField(verbose_name="협약기술기여도(3차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate4 = models.DecimalField(verbose_name="협약기술기여도(4차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate5 = models.DecimalField(verbose_name="협약기술기여도(5차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate6 = models.DecimalField(verbose_name="협약기술기여도(6차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    agreerate7 = models.DecimalField(verbose_name="협약기술기여도(7차년도)", max_digits=7, decimal_places=5, null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.company and self.project:
            self.name = f"{self.project.agency_info.name}_{self.project.title2}_{self.company.name}"
            self.unique_key = f"{self.project.project_id}_{self.company.company_id}"
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "실시기관별 과제"
        verbose_name_plural = "실시기관별 과제"
    def __str__(self):
        return f"{self.name}"
    
class NoSaleReason(models.Model):
    # agency_info = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name='전담기관정보', null=True, blank=True)
    uppercategory = models.CharField(max_length=50, verbose_name="상위 카테고리", null=True, blank=True)
    lowercategory = models.CharField(max_length=50, verbose_name="하위 카테고리", null=True, blank=True)
    contents = models.CharField(max_length=50, verbose_name="항목", null=True, blank=True)
    class Meta:
        verbose_name = "전담기관별 미실시 사유"
        verbose_name_plural = "전담기관별 미실시 사유"
    