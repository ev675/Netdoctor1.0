from fastapi import APIRouter

from app.schemas.dashboard import (
    DashboardOverview,
    DestinationResult,
    DiagnosisLayer,
    DiagnosisSummary,
    DnsServerResult,
    HealthScore,
    Metric,
    NetworkInfo,
    TracerouteHop,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/overview",
    response_model=DashboardOverview,
)
async def get_dashboard_overview():
    """
    Temporary dashboard data contract.

    In later phases these values will come from:
    Agent -> Measurements -> PostgreSQL -> Diagnosis Engine.
    """

    return DashboardOverview(
        health_score=HealthScore(
            score=72,
            status="FAIR",
            message="Your internet is not stable",
        ),

        latency=Metric(
            value=38,
            unit="ms",
            status="GOOD",
            min_value=22,
            max_value=78,
        ),

        jitter=Metric(
            value=61,
            unit="ms",
            status="POOR",
            min_value=11,
            max_value=142,
        ),

        packet_loss=Metric(
            value=4.2,
            unit="%",
            status="POOR",
            min_value=0,
            max_value=12.8,
        ),

        dns_latency=Metric(
            value=21,
            unit="ms",
            status="GOOD",
            min_value=12,
            max_value=45,
        ),

        download_mbps=92.4,
        upload_mbps=21.6,

        network=NetworkInfo(
            name="Home_WIFI_5G",
            connection_type="Wi-Fi",
            status="CONNECTED",
            ip_address="10.48.25.67",
            isp="Airtel Broadband",
        ),

        diagnosis_layers=[
            DiagnosisLayer(
                name="Device",
                status="GOOD",
                message="Your device is working fine.",
            ),
            DiagnosisLayer(
                name="Router / Wi-Fi",
                status="GOOD",
                message="Connection to router is stable.",
            ),
            DiagnosisLayer(
                name="ISP Gateway",
                status="GOOD",
                message="ISP gateway is reachable.",
            ),
            DiagnosisLayer(
                name="Internet Path",
                status="PROBLEM",
                message="Issues detected in the route.",
            ),
            DiagnosisLayer(
                name="Destination",
                status="DEGRADED",
                message="Some destinations are affected.",
            ),
        ],

        diagnosis_summary=DiagnosisSummary(
            title="Network Instability Detected",
            severity="HIGH",
            likely_problem_area="ISP / Upstream Network",
            confidence=81,
            evidence=[
                "Local gateway is healthy",
                "DNS response is within normal range",
                "Latency increases significantly after hop 6",
                "Packet loss begins downstream",
                "Multiple destinations show degradation",
            ],
        ),

        traceroute=[
            TracerouteHop(
                hop=1,
                ip_address="192.168.1.1",
                hostname="router.local",
                latency_ms=2,
                packet_loss_percent=0,
            ),
            TracerouteHop(
                hop=2,
                ip_address="100.64.0.1",
                hostname="100.64.0.1",
                latency_ms=15,
                packet_loss_percent=0,
            ),
            TracerouteHop(
                hop=3,
                ip_address="122.160.20.1",
                hostname="122.160.20.1",
                latency_ms=18,
                packet_loss_percent=0,
            ),
            TracerouteHop(
                hop=4,
                ip_address="122.160.8.145",
                hostname="122.160.8.145",
                latency_ms=21,
                packet_loss_percent=0,
            ),
            TracerouteHop(
                hop=5,
                ip_address="106.193.6.21",
                hostname="106.193.6.21",
                latency_ms=28,
                packet_loss_percent=0,
            ),
            TracerouteHop(
                hop=6,
                ip_address="72.14.197.93",
                hostname="72.14.197.93",
                latency_ms=142,
                packet_loss_percent=6,
            ),
            TracerouteHop(
                hop=7,
                ip_address="108.170.252.97",
                hostname="108.170.252.97",
                latency_ms=148,
                packet_loss_percent=6,
            ),
            TracerouteHop(
                hop=8,
                ip_address="142.250.74.78",
                hostname="142.250.74.78",
                latency_ms=145,
                packet_loss_percent=7,
            ),
        ],

        dns_benchmark=[
            DnsServerResult(
                server="Cloudflare (1.1.1.1)",
                latency_ms=18,
                status="GOOD",
            ),
            DnsServerResult(
                server="Google (8.8.8.8)",
                latency_ms=24,
                status="GOOD",
            ),
            DnsServerResult(
                server="Quad9 (9.9.9.9)",
                latency_ms=31,
                status="GOOD",
            ),
            DnsServerResult(
                server="OpenDNS",
                latency_ms=45,
                status="FAIR",
            ),
            DnsServerResult(
                server="ISP DNS",
                latency_ms=82,
                status="POOR",
            ),
        ],

        top_destinations=[
            DestinationResult(
                destination="google.com",
                latency_ms=28,
                status="GOOD",
            ),
            DestinationResult(
                destination="youtube.com",
                latency_ms=145,
                status="POOR",
            ),
            DestinationResult(
                destination="facebook.com",
                latency_ms=32,
                status="GOOD",
            ),
            DestinationResult(
                destination="github.com",
                latency_ms=30,
                status="GOOD",
            ),
        ],
    )