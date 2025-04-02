from django.db import models
from kimst.utils import proof_file_dir, process_upgrade_file_dir, form1_file_dir, form2_file_dir, form3_file_dir, form4_file_dir, form5_file_dir, form6_file_dir, folder_link, ntis_capture_file_dir

class Report(models.Model):
    iris_code = models.CharField(max_length=20, verbose_name="아이리스코드", null=True, blank=True)
    businessname1 = models.CharField(max_length=255, verbose_name="사업명", null=True, blank=True)
    businessname2 = models.CharField(max_length=255, verbose_name="내역사업명", null=True, blank=True)
    title1 = models.CharField(max_length=255, verbose_name="최상위과제명", null=True, blank=True)
    title2 = models.CharField(max_length=255, verbose_name="세부과제명", null=True, blank=True)
    t_dateengage = models.DateField(verbose_name="총 연구협약일", null=True, blank=True)
    t_datestart = models.DateField(verbose_name="총 연구개발시작일", null=True, blank=True)
    t_dateend = models.DateField(verbose_name="총 연구개발종료일", null=True, blank=True)
    c_datestart = models.DateField(verbose_name="총 연구개발시작일", null=True, blank=True)
    c_dateend = models.DateField(verbose_name="총 연구개발종료일", null=True, blank=True)
    maincompany = models.CharField(max_length=100, verbose_name="주관연구기관", null=True, blank=True)
    mainresearcher = models.CharField(max_length=100, verbose_name="주관연구책임자", null=True, blank=True)

    company = models.CharField(max_length=100, verbose_name="연구개발성과소유기관", null=True, blank=True)
    researcher = models.CharField(max_length=100, verbose_name="연구개발성과소유기관 책임자", null=True, blank=True)
    type = models.CharField(max_length=50, verbose_name="기업타입", null=True, blank=True)
    rate_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="기업요율")

    costgov = models.IntegerField(verbose_name="기업연구개발비(정부)", null=True, blank=True)
    costcompany = models.IntegerField(verbose_name="기업연구개발비(기업)", null=True, blank=True)
    costregion = models.IntegerField(verbose_name="기업연구개발비(지방)", null=True, blank=True)
    costetc = models.IntegerField(verbose_name="기업연구개발비(기타)", null=True, blank=True)
    cost = models.IntegerField(verbose_name="기업연구개발비(합계)", null=True, blank=True)
    rate_gov = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="정부기여도")

    grant1 = models.IntegerField(verbose_name="정산지원금(1차년도)", null=True, blank=True)
    grant2 = models.IntegerField(verbose_name="정산지원금(2차년도)", null=True, blank=True)
    grant3 = models.IntegerField(verbose_name="정산지원금(3차년도)", null=True, blank=True)
    grant4 = models.IntegerField(verbose_name="정산지원금(4차년도)", null=True, blank=True)
    grant5 = models.IntegerField(verbose_name="정산지원금(5차년도)", null=True, blank=True)
    grant6 = models.IntegerField(verbose_name="정산지원금(6차년도)", null=True, blank=True)
    grant7 = models.IntegerField(verbose_name="정산지원금(7차년도)", null=True, blank=True)
    grant8 = models.IntegerField(verbose_name="정산지원금(8차년도)", null=True, blank=True)
    grant9 = models.IntegerField(verbose_name="정산지원금(9차년도)", null=True, blank=True)
    grant10 = models.IntegerField(verbose_name="정산지원금(10차년도)", null=True, blank=True)

    obli = models.BooleanField(verbose_name="기술료 납부의무 여부", null=True, blank=True)
    closer = models.BooleanField(verbose_name="폐업 여부", null=True, blank=True)
    
    submit_status = models.BooleanField(verbose_name="제출 여부", null=True, blank=True)
    sales_status = models.BooleanField(verbose_name="매출발생 여부", null=True, blank=True)

    # 직접실시
    sales = models.IntegerField(verbose_name="매출발생금액(공급가액)", null=True, blank=True)
    rate_sales = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="매출기여도")
    




class Report_type1(models.Model):
    # 보고자 작성 부분
    # uniqueobject = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='과제고유정보', null=True, blank=True)
    proof_file = models.FileField(upload_to=proof_file_dir, verbose_name="매출증빙자료", null=True, blank=True)
    year = models.IntegerField(verbose_name="당해년도", null=True, blank=True)
    session = models.IntegerField(verbose_name="보고연차", null=True, blank=True)
    itemname = models.CharField(max_length=50, verbose_name="아이템명", null=True, blank=True)
    itemsalesamount = models.IntegerField(verbose_name="아이템매출액", null=True, blank=True)
    itemdetail = models.TextField(verbose_name="세부사양", null=True, blank=True)
    business_name = models.CharField(max_length=30, verbose_name="사업명", null=True, blank=True)
    business_feature = models.CharField(max_length=30, verbose_name="사업화 특성", null=True, blank=True)
    business_contribution = models.CharField(max_length=30, verbose_name="사업의 기여율", null=True, blank=True)
    profit_recognition = models.TextField(verbose_name="성과수익 인식기준 개요", null=True, blank=True)
    revenue_contribution_reason = models.TextField(verbose_name="성과수익 및 기여율 산정 개요", null=True, blank=True)
    # 검토자 작성부분
    manager = models.CharField(max_length=30, verbose_name="검토매니저", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 상태
    status = models.CharField(max_length=10, verbose_name="진행상태", null=True, blank=True) #저장, 검토중, 확정, 반려
    comment = models.TextField(verbose_name="검토 코멘트", null=True, blank=True)
    
    class Meta:
        verbose_name = "직접실시 리스트"
        verbose_name_plural = "직접실시 리스트"
    # def __str__(self):
    #     return f"{self.uniqueobject}"
    
class Report_type2(models.Model):
    # uniqueobject = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='과제고유정보', null=True, blank=True)
    year = models.IntegerField(verbose_name="당해년도", null=True, blank=True)
    session = models.IntegerField(verbose_name="보고연차", null=True, blank=True)
    succession = models.BooleanField(verbose_name="기술료 승계 여부", null=True, blank=True)
    counterparty = models.CharField(max_length=30, verbose_name="대상기관", null=True, blank=True)
    contract_title = models.CharField(max_length=50, verbose_name="실시계약명", null=True, blank=True)
    contract_procedure = models.CharField(max_length=50, verbose_name="계약방식", null=True, blank=True)
    contract_value = models.IntegerField(verbose_name="계약금액", null=True, blank=True)
    contract_date = models.DateField(verbose_name="실시계약일", null=True, blank=True)
    contract_period = models.CharField(max_length=20, verbose_name="계약기간", null=True, blank=True)
    ip_type = models.CharField(max_length=20, verbose_name="지재권 종류", null=True, blank=True)
    right_type = models.CharField(max_length=20, verbose_name="실시권 유형", null=True, blank=True)
    sales_type = models.CharField(max_length=20, verbose_name="실시방법", null=True, blank=True)
    patent_title = models.CharField(max_length=20, verbose_name="특허(출원, 등록) 명칭", null=True, blank=True)
    patent_code = models.CharField(max_length=20, verbose_name="특허(출원, 등록) 번호", null=True, blank=True)
    patent_date = models.CharField(max_length=20, verbose_name="일자", null=True, blank=True)
    owner_name = models.CharField(max_length=20, verbose_name="소유기관 기관명", null=True, blank=True)
    owner_type = models.CharField(max_length=20, verbose_name="소유기관 유형", null=True, blank=True)
    owner_address = models.CharField(max_length=100, verbose_name="소유기관 주소", null=True, blank=True)
    owner_ceo = models.CharField(max_length=20, verbose_name="대표자", null=True, blank=True)
    owner_code = models.CharField(max_length=20, verbose_name="사업자번호", null=True, blank=True)
    owner_phone = models.CharField(max_length=20, verbose_name="전화번호", null=True, blank=True)
    owner_department = models.CharField(max_length=20, verbose_name="부서(담당자)", null=True, blank=True)
    owner_email = models.CharField(max_length=50, verbose_name="이메일", null=True, blank=True)
    
    receiving_name = models.CharField(max_length=20, verbose_name="제3자실시기관 기관명", null=True, blank=True)
    receiving_type = models.CharField(max_length=20, verbose_name="제3자실시기관 유형", null=True, blank=True)
    receiving_address = models.CharField(max_length=100, verbose_name="제3자실시기관 주소", null=True, blank=True)
    receiving_ceo = models.CharField(max_length=20, verbose_name="대표자", null=True, blank=True)
    receiving_code = models.CharField(max_length=20, verbose_name="사업자번호", null=True, blank=True)
    receiving_phone = models.CharField(max_length=20, verbose_name="전화번호", null=True, blank=True)
    receiving_department = models.CharField(max_length=20, verbose_name="부서(담당자)", null=True, blank=True)
    receiving_email = models.CharField(max_length=50, verbose_name="이메일", null=True, blank=True)

    collection_plan1_date = models.DateField(verbose_name="1차 징수계획 일자", null=True, blank=True)
    collection_plan1_amount = models.IntegerField(verbose_name="1차 징수계획 금액", null=True, blank=True)
    collection_plan2_date = models.DateField(verbose_name="2차 징수계획 일자", null=True, blank=True)
    collection_plan2_amount = models.IntegerField(verbose_name="2차 징수계획 금액", null=True, blank=True)
    collection_plan3_date = models.DateField(verbose_name="3차 징수계획 일자", null=True, blank=True)
    collection_plan3_amount = models.IntegerField(verbose_name="3차 징수계획 금액", null=True, blank=True)
    collection_plan4_date = models.DateField(verbose_name="4차 징수계획 일자", null=True, blank=True)
    collection_plan4_amount = models.IntegerField(verbose_name="4차 징수계획 금액", null=True, blank=True)
    collection_plan5_date = models.DateField(verbose_name="5차 징수계획 일자", null=True, blank=True)
    collection_plan5_amount = models.IntegerField(verbose_name="5차 징수계획 금액", null=True, blank=True)
    collection_plan_total_amount = models.IntegerField(verbose_name="총 징수계획 금액", null=True, blank=True)

    payment_plan1_date = models.DateField(verbose_name="1차 정부납부기술료 납부계획 일자", null=True, blank=True)
    payment_plan1_amount = models.IntegerField(verbose_name="1차 정부납부기술료 납부계획 금액", null=True, blank=True)
    payment_plan2_date = models.DateField(verbose_name="2차 정부납부기술료 납부계획 일자", null=True, blank=True)
    payment_plan2_amount = models.IntegerField(verbose_name="2차 정부납부기술료 납부계획 금액", null=True, blank=True)
    payment_plan3_date = models.DateField(verbose_name="3차 정부납부기술료 납부계획 일자", null=True, blank=True)
    payment_plan3_amount = models.IntegerField(verbose_name="3차 정부납부기술료 납부계획 금액", null=True, blank=True)
    payment_plan4_date = models.DateField(verbose_name="4차 정부납부기술료 납부계획 일자", null=True, blank=True)
    payment_plan4_amount = models.IntegerField(verbose_name="4차 정부납부기술료 납부계획 금액", null=True, blank=True)
    payment_plan5_date = models.DateField(verbose_name="5차 정부납부기술료 납부계획 일자", null=True, blank=True)
    payment_plan5_amount = models.IntegerField(verbose_name="5차 정부납부기술료 납부계획 금액", null=True, blank=True)
    payment_plan_total_amount = models.IntegerField(verbose_name="총 정부납부기술료 납부계획 금액", null=True, blank=True)

    first_collect_year = models.IntegerField(verbose_name="1차 기술료 징수년도", null=True, blank=True)
    end_year = models.IntegerField(verbose_name="연구개발과제 종료년도", null=True, blank=True)

    this_collection_date = models.DateField(verbose_name="당해년도 징수일시", null=True, blank=True)
    this_collection_session = models.IntegerField(verbose_name="당해년도 징수회차", null=True, blank=True)
    this_collection_amount = models.IntegerField(verbose_name="당해년도 징수금액", null=True, blank=True)
    this_real_counted = models.IntegerField(verbose_name="당해년도 예상납부대상액", null=True, blank=True)
    this_real_decision = models.IntegerField(verbose_name="당해년도 예상결정금액", null=True, blank=True)

    collection_real_amount = models.CharField(max_length=100, verbose_name="징수금액 리스트", blank=True, null=True)
    collection_real_counted = models.CharField(max_length=100, verbose_name="예상납부대상액 리스트", blank=True, null=True)
    collection_real_discount = models.CharField(max_length=100, verbose_name="실 감면금액 리스트", blank=True, null=True)
    collection_real_decision = models.CharField(max_length=100, verbose_name="결정금액 리스트", blank=True, null=True)

    young_hiring = models.IntegerField(verbose_name="청년고용 감면", null=True, blank=True)
    argent_hiring = models.IntegerField(verbose_name="사회경제적 긴금한 상황 감면", null=True, blank=True)
    nationwarning_hiring = models.IntegerField(verbose_name="국가안보관련 감면", null=True, blank=True)
    innovate_hiring = models.IntegerField(verbose_name="혁신성과 감면", null=True, blank=True)
    etc_hiring = models.IntegerField(verbose_name="기타 감면", null=True, blank=True)

    # 검토자 작성부분
    manager = models.CharField(max_length=30, verbose_name="검토매니저", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 상태
    status = models.CharField(max_length=10, verbose_name="진행상태", null=True, blank=True) #저장, 검토중, 확정, 반려
    comment = models.TextField(verbose_name="검토 코멘트", null=True, blank=True)

    class Meta:
        verbose_name = "제3자실시 보고내용"
        verbose_name_plural = "제3자실시 보고내용"
    # def __str__(self):
    #     return f"{self.uniqueobject}"

class Report_type3_ntis(models.Model):
    # 보고자 작성 부분
    # uniqueobject = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='과제고유정보', null=True, blank=True)
    year = models.IntegerField(verbose_name="당해년도", null=True, blank=True)
    session = models.IntegerField(verbose_name="보고연차", null=True, blank=True)
    ntis_capture_file = models.FileField(upload_to=ntis_capture_file_dir, verbose_name="ntis캡처 이미지", null=True, blank=True)
    status = models.CharField(max_length=10, verbose_name="진행상태", null=True, blank=True)#검토중, 반려, 확정
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "미실시 NTIS 캡처 업로드"
        verbose_name_plural = "미실시 NTIS 캡처 업로드"
    # def __str__(self):
    #     return f"{self.uniqueobject}"
    
class Report_type3_nosalereason(models.Model):
    # uniqueobject = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='과제고유정보', null=True, blank=True)
    year = models.IntegerField(verbose_name="당해년도", null=True, blank=True)
    session = models.IntegerField(verbose_name="보고연차", null=True, blank=True)
    uppercategory = models.CharField(max_length=50, verbose_name="상위 카테고리", null=True, blank=True)
    lowercategory = models.CharField(max_length=50, verbose_name="하위 카테고리", null=True, blank=True)
    contents = models.CharField(max_length=50, verbose_name="항목", null=True, blank=True)
    status = models.CharField(max_length=10, verbose_name="진행상태", null=True, blank=True) #검토중, 반려, 확정
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "미실시 사유"
        verbose_name_plural = "미실시 사유"
    # def __str__(self):
    #     return f"{self.uniqueobject}"