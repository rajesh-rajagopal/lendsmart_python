from lendsmart_api.jwt import Jwt


ISSUER = 'lendsmart_sh/serviceaccount'

SUBJECT = 'lendsmart_sh/serviceaccount/service-account.name'

# copy paste the private key generated for the service account
SECRET_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQM0Gb5uje/9XE
TgqlhMpX9XI1j2og4Smh+pxB7FYupKJWRA+cKdsVnyyn1fNERTYFZ4nh6q7SbIpi
KpoJ9WHWD35FgtZE8nCCvLS3wekpzxqppafaDdcoKBWu4vQXNmavqRRY+Z2oqeZF
0uKS9mNExcrMQGb0uEUrj9YyHY+fjmm2P3aIVe2X2NWrhNN6gwr2/dHK4OQmSYuA
tHyQUlPaC98eeKSRgMP/YIyHA6ysRJKF9RMtQppT0RGt9fvKKuJsCPeWnAwAZck7
NYm+12a/Ogs/yIkgWilLEgdW9Cae2WbRKOEPxIRHdAAO9YZw3vGjV2Bxj4sXHivl
wv4c1DAjAgMBAAECggEASjoL6Q4w9dgWGU+NgidOkH9kQW4o8yHzWtljPimJLEXr
zn+jZRSTFClUnV2sxik6skCQquelfkXOLGNt2aEPSWbqqNOVmq0oqaOndl/+xbYd
lmAF8LrAe4OW/2vQhDoT8AqCw5nyuIAiJcCioKyRBaLSw3Eug47ysi4sul9JpiNV
vxWbUe1kJXzQRgHKAO0XAKDcscgypGOfQcFbe6cNBcADlKf0KVVnTbw5laHry9pF
ZsIV0FKp3xPqnqq6cDjEextvQETlpq+RuDze96ZXMC4ZFjxPpSd7q/VNYIkCibk5
7Q07Z0CZMJxUGo+CCKO/m4zQ2lGH6hxrKm6VR2unyQKBgQD4x9VfozjB9NETKXLJ
zPYtf7PGU9GDIIlmEALnfPpETE/DdO6+O92rKStaLi98/F/D88XBgmejKyGYOrqb
D2Ah3SeHViSUxAFQBuLHq9/fn+S6tRkTMEW+2eiZMkq4VpvOpPpHQ7uKjeGwSf1Z
lnOUSiJCMU+lZEFiMUe1vzVnDQKBgQDWPfSFaG500/Z2Rjmc3xhEJJoAkTQfZa7t
Kcaumq88FVJidMm2dlB3dMEej5338U2+/ZCS+ZhK7LYpRkuXp8qDr1LsL0j/96YL
RLUzVliroojwYiF8pipXfkm/mJbFXirRl8YR+WUrisU4CemQSEh/h5fJ3LGwhPvT
JrTaAt4n7wKBgGs/0wfI2OYcwaluG/NNbe+NdxYP+ml6NGGQk3/yS/33nAdaOLZA
Hr70H6Ff+c77CdnzFJTov/8C0BfNcbb5OOtAaRMaGukbWqmCXm/P89J3HucyvV2d
WOP/ExxAJyAzDjZWvyLL22TO57XVH+hoSOlr0DsTAQ//GYTYU97RUJddAoGAI43M
kocuLX0vnZkx3nK3mDdqx0VRnRRG31zbeAZ7pkDzlxtCjmE8IVbi5at3z7nf6R4z
a/C38VcvM9JSoSxbU1c5L7D5MGFs0NnqKEbgGDu09g+S9xisVjDDFGTCQKbL/FRv
rnPw8jTpXc9nT2ZvgZqC+iEB7AVltTjrMnLfY0kCgYAjXVNxxsPmAYE24036zgCz
W3vN+v0C90KzrAbfa9tbYlZwktm5BBTwRW9Bgs3TCbXW5nEXxmpsHW8lpMtenpHh
PLcnNa/AfRP49dgii3hodXqh0yb8AAhrgZXz5bKK87Gt0rE6ZDIj86AlQL5pc/PM
LquyS5KBkzOmbRzr8qBcKA==
-----END PRIVATE KEY-----
"""

j = Jwt(SECRET_KEY, ISSUER, SUBJECT)

print j.to_jwt()
