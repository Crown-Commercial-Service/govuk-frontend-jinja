
import pytest


def test_file_upload(env):
    template = env.from_string(
"""
{% from "file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  "id": "file-upload-1",
  "name": "file-upload-1",
  "label": {
    "text": "Upload a file"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-1">
    Upload a file
  </label>

  <input class="govuk-file-upload" id="file-upload-1" name="file-upload-1" type="file">
</div>
"""
        )
    )


def test_file_upload_with_hint_text(env):
    template = env.from_string(
"""
{% from "file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  "id": "file-upload-2",
  "name": "file-upload-2",
  "label": {
    "text": "Upload your photo"
  },
  "hint": {
    "text": "Your photo may be in your Pictures, Photos, Downloads or Desktop folder. Or in an app like iPhoto."
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-2">
    Upload your photo
  </label>

  <span id="file-upload-2-hint" class="govuk-hint">
    Your photo may be in your Pictures, Photos, Downloads or Desktop folder. Or in an app like iPhoto.
  </span>

  <input class="govuk-file-upload" id="file-upload-2" name="file-upload-2" type="file" aria-describedby="file-upload-2-hint">
</div>
"""
        )
    )


def test_file_upload_with_error_message(env):
    template = env.from_string(
"""
{% from "file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  "id": "file-upload-3",
  "name": "file-upload-3",
  "label": {
    "text": "Upload a file"
  },
  "hint": {
    "text": "Your photo may be in your Pictures, Photos, Downloads or Desktop folder. Or in an app like iPhoto."
  },
  "errorMessage": {
    "text": "Error message goes here"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group govuk-form-group--error">
  <label class="govuk-label" for="file-upload-3">
    Upload a file
  </label>

  <span id="file-upload-3-hint" class="govuk-hint">
    Your photo may be in your Pictures, Photos, Downloads or Desktop folder. Or in an app like iPhoto.
  </span>

  <span id="file-upload-3-error" class="govuk-error-message">
    Error message goes here
  </span>

  <input class="govuk-file-upload govuk-file-upload--error" id="file-upload-3" name="file-upload-3" type="file" aria-describedby="file-upload-3-hint file-upload-3-error">
</div>
"""
        )
    )


def test_file_upload_with_value_and_attributes(env):
    template = env.from_string(
r"""
{% from "file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  "id": "file-upload-4",
  "name": "file-upload-4",
  "value": "C:\\fakepath\\myphoto.jpg",
  "label": {
    "text": "Upload a photo"
  },
  "attributes": {
    "accept": ".jpg, .jpeg, .png"
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
r"""
<div class="govuk-form-group">
  <label class="govuk-label" for="file-upload-4">
    Upload a photo
  </label>

  <input class="govuk-file-upload" id="file-upload-4" name="file-upload-4" type="file" value="C:\fakepath\myphoto.jpg" accept=".jpg, .jpeg, .png">
</div>
"""
        )
    )


def test_file_upload_with_label_as_page_heading(env):
    template = env.from_string(
"""
{% from "file-upload/macro.njk" import govukFileUpload %}

{{ govukFileUpload({
  "id": "file-upload-1",
  "name": "file-upload-1",
  "label": {
    "text": "Upload a file",
    "isPageHeading": true
  }
}) }}
"""
    )
    assert (
        pytest.helpers.normalise_whitespace(template.render())
        ==
        pytest.helpers.normalise_whitespace(
"""
<div class="govuk-form-group">
  <h1 class="govuk-label-wrapper">
    <label class="govuk-label" for="file-upload-1">
      Upload a file
    </label>

  </h1>

  <input class="govuk-file-upload" id="file-upload-1" name="file-upload-1" type="file">
</div>
"""
        )
    )
