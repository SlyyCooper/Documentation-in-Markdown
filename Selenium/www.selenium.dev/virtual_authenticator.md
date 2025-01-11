## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.virtual_authenticator](#seleniumwebdrivercommonvirtual_authenticator)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.virtual_authenticator

# selenium.webdriver.common.virtual_authenticator

Functions

`required_chromium_based_browser`(func) | A decorator to ensure that the client used is a chromium based browser.  
---|---  
`required_virtual_authenticator`(func) | A decorator to ensure that the function is called with a virtual authenticator.  
  
Classes

`Credential`(credential_id, ...) | Constructor.  
---|---  
`Protocol`(value) | Protocol to communicate with the authenticator.  
`Transport`(value) | Transport method to communicate with the authenticator.  
`VirtualAuthenticatorOptions`([protocol, ...]) | Constructor.  
  
_class
_selenium.webdriver.common.virtual_authenticator.Protocol(_value_)[source]

    

Protocol to communicate with the authenticator.

CTAP2 _: str_ _ = 'ctap2'_

    

U2F _: str_ _ = 'ctap1/u2f'_

    

_class
_selenium.webdriver.common.virtual_authenticator.Transport(_value_)[source]

    

Transport method to communicate with the authenticator.

BLE _: str_ _ = 'ble'_

    

USB _: str_ _ = 'usb'_

    

NFC _: str_ _ = 'nfc'_

    

INTERNAL _: str_ _ = 'internal'_

    

_class
_selenium.webdriver.common.virtual_authenticator.VirtualAuthenticatorOptions(_protocol
: str = Protocol.CTAP2_, _transport : str = Transport.USB_, _has_resident_key
: bool = False_, _has_user_verification : bool = False_, _is_user_consenting :
bool = True_, _is_user_verified : bool = False_)[source]

    

Constructor.

Initialize VirtualAuthenticatorOptions object.

_class _Protocol(_value_)

    

Protocol to communicate with the authenticator.

CTAP2 _: str_ _ = 'ctap2'_

    

U2F _: str_ _ = 'ctap1/u2f'_

    

_class _Transport(_value_)

    

Transport method to communicate with the authenticator.

BLE _: str_ _ = 'ble'_

    

USB _: str_ _ = 'usb'_

    

NFC _: str_ _ = 'nfc'_

    

INTERNAL _: str_ _ = 'internal'_

    

to_dict() -> Dict[str, str | bool][source]
    

_class _selenium.webdriver.common.virtual_authenticator.Credential(_credential_id : bytes_, _is_resident_credential : bool_, _rp_id : str_, _user_handle : bytes | None_, _private_key : bytes_, _sign_count : int_)[source]
    

Constructor. A credential stored in a virtual authenticator.
https://w3c.github.io/webauthn/#credential-parameters.

Args:

    

  * credential_id (bytes): Unique base64 encoded string.

is_resident_credential (bool): Whether the credential is client-side
discoverable. rp_id (str): Relying party identifier. user_handle (bytes):
userHandle associated to the credential. Must be Base64 encoded string. Can be
None. private_key (bytes): Base64 encoded PKCS#8 private key. sign_count
(int): intital value for a signature counter.

_property _id _: str_

    

_property _is_resident_credential _: bool_

    

_property _rp_id _: str_

    

_property _user_handle _: str | None_
    

_property _private_key _: str_

    

_property _sign_count _: int_

    

_classmethod _create_non_resident_credential(_id : bytes_, _rp_id : str_,
_private_key : bytes_, _sign_count : int_) -> Credential[source]

    

Creates a non-resident (i.e. stateless) credential.

Args:

    

  * id (bytes): Unique base64 encoded string.

  * rp_id (str): Relying party identifier.

  * private_key (bytes): Base64 encoded PKCS

  * sign_count (int): intital value for a signature counter.

Returns:

    

  * Credential: A non-resident credential.

_classmethod _create_resident_credential(_id : bytes_, _rp_id : str_, _user_handle : bytes | None_, _private_key : bytes_, _sign_count : int_) -> Credential[source]
    

Creates a resident (i.e. stateful) credential.

Args:

    

  * id (bytes): Unique base64 encoded string.

  * rp_id (str): Relying party identifier.

  * user_handle (bytes): userHandle associated to the credential. Must be Base64 encoded string.

  * private_key (bytes): Base64 encoded PKCS

  * sign_count (int): intital value for a signature counter.

Returns:

    

  * Credential: A resident credential.

to_dict() -> Dict[str, Any][source]

    

_classmethod _from_dict(_data : Dict[str, Any]_) -> Credential[source]

    

selenium.webdriver.common.virtual_authenticator.required_chromium_based_browser(_func_)[source]

    

A decorator to ensure that the client used is a chromium based browser.

selenium.webdriver.common.virtual_authenticator.required_virtual_authenticator(_func_)[source]

    

A decorator to ensure that the function is called with a virtual
authenticator.

### Table of Contents

  * selenium.webdriver.common.virtual_authenticator
    * `Protocol`
      * `Protocol.CTAP2`
      * `Protocol.U2F`
    * `Transport`
      * `Transport.BLE`
      * `Transport.USB`
      * `Transport.NFC`
      * `Transport.INTERNAL`
    * `VirtualAuthenticatorOptions`
      * `VirtualAuthenticatorOptions.Protocol`
        * `VirtualAuthenticatorOptions.Protocol.CTAP2`
        * `VirtualAuthenticatorOptions.Protocol.U2F`
      * `VirtualAuthenticatorOptions.Transport`
        * `VirtualAuthenticatorOptions.Transport.BLE`
        * `VirtualAuthenticatorOptions.Transport.USB`
        * `VirtualAuthenticatorOptions.Transport.NFC`
        * `VirtualAuthenticatorOptions.Transport.INTERNAL`
      * `VirtualAuthenticatorOptions.to_dict()`
    * `Credential`
      * `Credential.id`
      * `Credential.is_resident_credential`
      * `Credential.rp_id`
      * `Credential.user_handle`
      * `Credential.private_key`
      * `Credential.sign_count`
      * `Credential.create_non_resident_credential()`
      * `Credential.create_resident_credential()`
      * `Credential.to_dict()`
      * `Credential.from_dict()`
    * `required_chromium_based_browser()`
    * `required_virtual_authenticator()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.virtual_authenticator

(C) Copyright 2009-2024 Software Freedom Conservancy.