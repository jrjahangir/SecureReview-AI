from datetime import datetime
import os


def generate_report_filename(original_filename, extension):
    """
    Generate a unique report filename.

    Example:
    FSecurityTest_20260712_181530.html
    """

    # Remove extension from uploaded file
    base_name = os.path.splitext(original_filename)[0]

    # Replace spaces with underscores
    base_name = base_name.replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{base_name}_{timestamp}.{extension}"