#TODO: CREATE A CUSTOM PERMISSION THAT WILL MAKE SURE THAT
# IT CHECKS THE AUTHENTICATED USER ID AS THE SAME AS THE READER USER ID

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# IsAuthenticated -> If user is not authenticated, it will fail
# IsAdminUser -> 'is_staff' is 'False', it will fail
# IsAuthenticatedOrReadOnly ->
    # POST
    # GET           -> Read
    # PUT, PATCH
    # DELETE