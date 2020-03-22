from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_iam as iam,
    aws_s3_deployment as s3deploy
)

class CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        bucket: s3.Bucket = s3.Bucket(self, "Bucket", website_index_document="index.html")
        origin = cloudfront.OriginAccessIdentity(self, "BucketOrigin", comment="mythical-mysfits")
        bucket.grant_read(iam.CanonicalUserPrincipal(origin.cloud_front_origin_access_identity_s3_canonical_user_id))
        cdn = cloudfront.CloudFrontWebDistribution(
            self,
            "CloudFront",
            viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.ALLOW_ALL,
            price_class=cloudfront.PriceClass.PRICE_CLASS_ALL,
            origin_configs=[cloudfront.SourceConfiguration(
                s3_origin_source=cloudfront.S3OriginConfig(
                    s3_bucket_source=bucket,
                    origin_access_identity=origin
                ),
                behaviors=[cloudfront.Behavior(is_default_behavior=True, allowed_methods=cloudfront.CloudFrontAllowedMethods.GET_HEAD_OPTIONS)],
                origin_path="/web"
            )]
        )
        s3deploy.BucketDeployment(
            self,
            "DeployWebsite",
            sources=[s3deploy.Source.asset('../web')],
            destination_key_prefix= "web/",
            destination_bucket=bucket,
            distribution
        )


# new s3deploy.BucketDeployment(this, "DeployWebsite", {
#   sources: [
#     s3deploy.Source.asset(webAppRoot)
#   ],
#   destinationKeyPrefix: "web/",
#   destinationBucket: bucket,
#   distribution: cdn,
#   retainOnDelete: false
# });
