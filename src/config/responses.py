from fastapi.responses import JSONResponse

DEFAULT_RESPONSE = {
  "error": None,
  "data": None 
}

# Custom response function to standardize API responses
custom_response = lambda data, error = None, status = 200, is_swagger = False: JSONResponse(
  status_code=status,
  content={
    "error": error,
    "data": data
  }
) if not is_swagger else { "error": error, "data": data }