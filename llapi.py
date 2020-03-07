import ctypes
import os

path = '/g/g0/defazio1/lustre-release/lustre/utils/.libs/liblustreapi.so.1.0.0'
lustreapi = ctypes.cdll.LoadLibrary(path)

lustreapi.llapi_exceeded_quota.argtypes = [ctypes.c_char_p, ctypes.c_int]

def exceeding_lustre_quota(fsname, uid):
    '''wraps llapi_exceeding_quota to make it more
    pythonic. Allows use of normal strings, performs type checks,
    gives error messages.'''
    _fsname = None
    if isinstance(fsname, bytes):
        _fsname = fsname
    elif isinstance(fsname, str):
        _fsname = fsname.encode()
        
    edquot = lustreapi.llapi_exceeded_quota(_fsname, uid)

    # success 
    if edquot == 0 or edquot == 1:
        return bool(edquot)
    # some errno failure
    elif edquot < 0:
        return os.strerror(-edquot)
    # unrecognized error    
    else:
        raise RuntimeError('unexpected return value from' +
                           ' C function llapi_exceeding_quota()')
        
    

    


