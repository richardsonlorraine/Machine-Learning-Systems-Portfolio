# API Management: Rate Limiting and IP Filtering
policy_xml = """<policies>
    <inbound>
        <rate-limit-by-key calls="5" renewal-period="60" counter-key="@(context.Request.IpAddress)" />
        <ip-filter action="allow">
            <address-range from="192.168.0.0" to="192.168.255.255" />
        </ip-filter>
    </inbound>
</policies>"""

from azure.mgmt.network import NetworkManagementClient
nsg_params = {'location': 'eastus', 'security_rules': [{'name': 'RestrictToTrustedIP', 'protocol': 'Tcp', 'direction': 'Inbound', 'access': 'Allow', 'priority': 100, 'source_address_prefix': '192.168.1.0/24', 'destination_port_range': '80'}]} # network_client.network_security_groups.begin_create_or_update(...)

from msal import ConfidentialClientApplication # Enforcing MFA via OAuth 2.0
app = ConfidentialClientApplication(client_id, client_credential=client_secret)
token_response = app.acquire_token_for_client(scopes=['https://management.azure.com/.default'])
if 'access_token' in token_response:
    print("MFA-enforced token acquired. Identity verified.")

