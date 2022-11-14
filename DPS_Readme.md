Use _OpenSSL_ to create a _self-signed X.509 certificate_ and a _private key_. This certificate will be uploaded to your provisioning service instance and verified by the service.

```
winpty openssl req -outform PEM -x509 -sha256 -newkey rsa:4096 -keyout device-key.pem -out device-cert.pem -days 30 -extensions usr_cert -addext extendedKeyUsage=clientAuth -subj "//CN=my-x509-device"
```

Enter PEM pass phrase

## Add the device to DPS

1. Sign in to the Azure portal.

2. On the left-hand menu or on the portal page, select All resources.

3. Select your Device Provisioning Service.

4. In the Settings menu, select Manage enrollments.

5. At the top of the page, select + Add individual enrollment.

6. In the Add Enrollment page, enter the following information.

- Mechanism: Select X.509 as the identity attestation Mechanism.
- Primary certificate .pem or .cer file: Choose Select a file and navigate to and select the certificate file, device-cert.pem, that you created in the previous section.
- Leave IoT Hub Device ID: blank. Your device will be provisioned with its device ID set to the common name (CN) in the X.509 certificate. This common name will also be the name used for the registration ID for the individual enrollment entry.

7. Select Save. You'll be returned to Manage enrollments.

8. Select Individual Enrollments. Your X.509 enrollment entry, __deviceId__, should appear in the list.


## Prepare the code

```python
provisioning_host = "global.azure-devices-provisioning.net"
id_scope = "0ne00848CFC"
registration_id = "deviceId"
```
### Define variables

- PROVISIONING_HOST: The global endpoint used for connecting to your DPS instance.
- PROVISIONING_IDSCOPE: The ID Scope for your DPS instance.
- DPS_X509_REGISTRATION_ID: The registration ID for your device. It must also match the subject name on the device certificate.
- X509_CERT_FILE: The path to your device certificate file.
- X509_KEY_FILE: The path to your device certificate private key file.
- PASS_PHRASE: The pass phrase you used to encrypt the certificate and private key file (sngular).

### Execute the code!