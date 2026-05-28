from django.apps import AppConfig


class MxrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mxr'
    verbose_name = "MXRemastered"
    is_modular = True
    root_url = "/MXRemastered"
    icon = "🗄️"

    def get_dashboard_stats(self):
        successfull_calls = 200
        failed_calls = 20

        return {
            "(WIP)Successfull calls": successfull_calls,
            "(WIP)Failed calls": failed_calls
        }
    