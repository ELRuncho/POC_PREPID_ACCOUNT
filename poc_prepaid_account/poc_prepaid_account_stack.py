from aws_cdk import (
    core as cdk,
    aws_servicecatalog as servicecatalog
)
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class PocPrepaidAccountStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        portfolio = servicecatalog.Portfolio(self, "SandboxAccount",
            display_name="SandboxAccount",
            provider_name="AWS sandbox account",
            accept_language=servicecatalog.AcceptLanguage.EN 
        )

        artifactsparam = servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty(info={
                                                                                                                "LoadTemplateFromURL":"https://raw.githubusercontent.com/ELRuncho/POC_PREPID_ACCOUNT/main/sanbox-start.yaml"
                                                                                                              },
                                                                                                                    name="June 2021" ,
                                                                                                                    description="June 2021"
                                                                                                                )

        cfnProduct= servicecatalog.CfnCloudFormationProduct(self, "Sandbox Account",
            name="Sandbox Account",
            owner="Octank",
            support_email="support@yourcompany.com",
            support_url="https://www.amazon.com",
            provisioning_artifact_parameters=[artifactsparam]
        )

        servicecatalog.CfnPortfolioProductAssociation(self, "sandboxassociation",
                    product_id= cfnProduct.ref ,
                    portfolio_id= portfolio.portfolio_id
        )



