def validate_product(prod_no, prod_name, prod_price, prod_quantity):
    """Validate product input data"""
    try:
        if not all([prod_no, prod_name, prod_price, prod_quantity]):
            return False, "All fields are required"
        
        if not str(prod_no).isdigit():
            return False, "Product number must be numeric"
            
        if not str(prod_price).replace('.','',1).isdigit():
            return False, "Price must be numeric"
            
        if not str(prod_quantity).isdigit():
            return False, "Quantity must be numeric"
            
        return True, "Valid input"
    except Exception as e:
        return False, f"Validation error: {str(e)}"
