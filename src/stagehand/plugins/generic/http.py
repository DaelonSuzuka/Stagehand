import httpx
from stagehand.sandbox import Sandbox, SandboxExtension


class HttpExtension(SandboxExtension):
    """HTTP client extension for making requests from sandbox scripts.
    
    Available in sandbox as: http.get(), http.post(), etc.
    
    Example:
        # Simple GET request
        response = http.get('https://api.example.com/data')
        print(response.text)
        
        # POST with JSON
        response = http.post('https://api.example.com/users', json={'name': 'Alice'})
        print(response.json())
        
        # With headers
        response = http.get('https://api.example.com/protected', 
            headers={'Authorization': 'Bearer token123'})
    """
    
    name = 'http'
    
    def __init__(self):
        self._client = httpx.Client()
        self._async_client = None
    
    def request(self, method: str, url: str, **kwargs):
        """Send an HTTP request.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            url: Request URL
            **kwargs: Additional arguments passed to httpx
                - params: Query parameters dict
                - headers: Request headers dict
                - json: JSON body (auto-serialized)
                - data: Request body (form data, etc.)
                - timeout: Request timeout in seconds
                
        Returns:
            Response object with .text, .json(), .status_code, .headers
        """
        try:
            response = self._client.request(method, url, **kwargs)
            return response
        except Exception as e:
            Sandbox().tools.print(f'HTTP request failed: {e}')
            raise
    
    def get(self, url: str, **kwargs):
        """Send a GET request.
        
        Args:
            url: Request URL
            **kwargs: params, headers, timeout, etc.
                
        Returns:
            Response object
        """
        return self.request('GET', url, **kwargs)
    
    def post(self, url: str, **kwargs):
        """Send a POST request.
        
        Args:
            url: Request URL
            **kwargs: json, data, headers, etc.
                
        Returns:
            Response object
        """
        return self.request('POST', url, **kwargs)
    
    def put(self, url: str, **kwargs):
        """Send a PUT request.
        
        Args:
            url: Request URL
            **kwargs: json, data, headers, etc.
                
        Returns:
            Response object
        """
        return self.request('PUT', url, **kwargs)
    
    def patch(self, url: str, **kwargs):
        """Send a PATCH request.
        
        Args:
            url: Request URL
            **kwargs: json, data, headers, etc.
                
        Returns:
            Response object
        """
        return self.request('PATCH', url, **kwargs)
    
    def delete(self, url: str, **kwargs):
        """Send a DELETE request.
        
        Args:
            url: Request URL
            **kwargs: headers, etc.
                
        Returns:
            Response object
        """
        return self.request('DELETE', url, **kwargs)
    
    def head(self, url: str, **kwargs):
        """Send a HEAD request.
        
        Args:
            url: Request URL
            **kwargs: headers, etc.
                
        Returns:
            Response object
        """
        return self.request('HEAD', url, **kwargs)
    
    def options(self, url: str, **kwargs):
        """Send an OPTIONS request.
        
        Args:
            url: Request URL
            **kwargs: headers, etc.
                
        Returns:
            Response object
        """
        return self.request('OPTIONS', url, **kwargs)
    
    def close(self):
        """Close the HTTP client. Called automatically on app exit."""
        self._client.close()