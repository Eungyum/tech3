from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MemberUser
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MemberUserResource(resources.ModelResource):
    class Meta:
        model = MemberUser
        # 엑셀 업로드/다운로드시 사용할 필드 지정 (원하는 필드만 지정 가능)
        fields = ('id', 'username', 'email', 'role', 'is_staff', 'is_active',)
        export_order = ('id', 'username', 'email', 'role', 'is_staff', 'is_active',)

@admin.register(MemberUser)
class MemberUserAdmin(ImportExportModelAdmin, UserAdmin):
    """
    기본 UserAdmin, form 상속
    role 필드 추가
    """
    # 사용자 수정 페이지에서 보여지는 필드 그룹 설정
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'full_name', 'phone1','phone2','department', 'companylogo')}),
    )
    # 새 사용자 추가할 때 표시되는 필드 그룹
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'full_name', 'phone1','phone2','department', 'companylogo')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')

admin.site.site_title = "기술료 관리 시스템"
admin.site.site_header = "기술료 어드민 페이지" 
admin.site.index_title = "관리 페이지 홈"